from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask import session,request
from user.mail_verify import email


db = MySQL()

class AdminOtherTableData:
    def __init__(self):
        pass

    def admin_other_table_data(self):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM admin_login")
            admin_other_data = cur.fetchall()
            if admin_other_data:
                return admin_other_data
            else:
                return "no admin"
        except Exception as e:
            print(e)
            return "no admin"
        

    def delete_other_admin_data_in_admin(self,other_admin_id):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM admin_login WHERE id=%s",(other_admin_id,))
            user_data = cur.fetchone()
            if user_data:
                cur.execute("DELETE FROM admin_login WHERE id=%s",(other_admin_id,))
                db.connection.commit()
                cur.close()
                return "delete"
            else:
                return "failed"
        except Exception as e:
            print(e)
            return "failed"