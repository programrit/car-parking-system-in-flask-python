from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask import session,request
from user.mail_verify import email
from flask_bcrypt import Bcrypt


db = MySQL()
bcrypt = Bcrypt()
class AdminTableData:
    def __init__(self):
        pass

    def current_admin_data(self):
        try:
            admin_id = session['admin_id']
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM admin WHERE admin_id=%s",(admin_id,))
            current_admin_data = cur.fetchone()
            if current_admin_data:
                return current_admin_data
            else:
                return "no admin"
        except Exception as e:
            print(e)
            return "no admin"

    def admins_data(self):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM admin")
            admin_data = cur.fetchall()
            if admin_data:
                return admin_data
            else:
                return "no admin"
        except Exception as e:
            print(e)
            return "no admin"
        
    def add_new_admin_in_admin(self,user_id,name,gmail,password):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM admin WHERE email = %s", (gmail,))
            email_exist = cur.fetchone()
            if email_exist:
                return "email exist"
            else:
                send_email = email(gmail)
                send_password = send_email.send_password(name,password)
                if send_password == "send":
                    password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
                    cur.execute("INSERT INTO admin (admin_id,name,email,password) VALUES (%s,%s,%s,%s)",(user_id,name,gmail,password_hash))
                    db.connection.commit()
                    cur.close()
                    return "add"
                else:
                    return "not send"
        except Exception as e:
            print(e)
            return "not add"
        
    def delete_admin_data_in_admin(self,admin_id):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM admin WHERE id=%s",(admin_id,))
            admin_value = cur.fetchone()
            if admin_value:
                cur.execute("DELETE FROM admin WHERE id=%s",(admin_id,))
                db.connection.commit()
                cur.close()
                return "delete"
            else:
                return "failed"
        except Exception as e:
            print(e)
            return "failed"