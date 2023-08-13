from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask import session,request
from user.mail_verify import email


db = MySQL()

class UserTableData:
    def __init__(self):
        pass

    def users_data(self):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM user")
            user_other_data = cur.fetchall()
            if user_other_data:
                return user_other_data
            else:
                return "no users"
        except Exception as e:
            print(e)
            return "no users"
        

    def add_new_user_in_admin(self,user_id,name,mobile,gmail,password_hash,confirm_password_hash):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM user WHERE email = %s", (gmail,))
            email_exist = cur.fetchone()
            if email_exist:
                return "email exist"
            else:
                cur.execute("SELECT * FROM user WHERE phone_no = %s", (mobile,))
                phone_exist = cur.fetchone()
                if phone_exist:
                    return "phone exist"
                else:
                    cur.execute("INSERT INTO user (user_id,name,phone_no,email,password,confirm_password) VALUES (%s,%s,%s,%s,%s,%s)",(user_id,name,mobile,gmail,password_hash,confirm_password_hash))
                    db.connection.commit()
                    cur.close()
                    return "add"
        except Exception as e:
            print(e)
            return "not add"
        


    def send_data_update(self,user_id):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM user WHERE id=%s",(user_id,))
            user_data = cur.fetchone()
            if user_data:
                return user_data
            else:
                return "no user"
        except Exception as e:
            print(e)
            return "no user"
        
    
    def update_user_data_in_admin(self,user_id,name):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM WHERE id=%s",(user_id,))
            fetch_data = cur.fetchone()
            if fetch_data:
                cur.execute("UPDATE user SET name=%s WHERE id=%s",(name,user_id))
                db.connection.commit()
                cur.close()
                return "update"
            else:
                return "failed"
        except Exception as e:
            print(e)
            return "failed"
        
    def delete_user_data_in_admin(self,delete_id):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM user WHERE id=%s",(delete_id,))
            fetch_data = cur.fetchone()
            if fetch_data:
                cur.execute("DELETE FROM user WHERE id=%s",(delete_id,))
                db.connection.commit()
                cur.close()
                return "delete"
            else:
                return "failed"
        except Exception as e:
            print(e)
            return "failed"