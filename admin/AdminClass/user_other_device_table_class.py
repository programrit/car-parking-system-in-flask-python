from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask import session,request
from user.mail_verify import email


db = MySQL()

class UserOtherTableData:
    def __init__(self):
        pass

    def user_other_table_data(self):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM user_login")
            user_other_table_data = cur.fetchall()
            if user_other_table_data:
                return user_other_table_data
            else:
                return "no users"
        except Exception as e:
            print(e)
            return "no users"
        
    def delete_other_user_data_in_admin(self,other_user_id):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM user_login WHERE id=%s",(other_user_id,))
            user_data = cur.fetchone()
            if user_data:
                cur.execute("DELETE FROM user_login WHERE id=%s",(other_user_id,))
                db.connection.commit()
                cur.close()
                return "delete"
            else:
                return "failed"
        except Exception as e:
            print(e)
            return "failed"
