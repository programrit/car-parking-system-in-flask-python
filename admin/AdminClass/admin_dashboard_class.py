from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask import session,request
from user.mail_verify import email


db = MySQL()

class AdminDashboardVerify:
    def __init__(self):
        pass

    def admin_is_found_or_not(self):
        try:
            admin_id = session['admin_id']
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM admin WHERE admin_id = %s", (admin_id,))
            admin_exist = cur.fetchone()
            if admin_exist:
                return "admin"
            else:
                return "admin not found"
        except Exception as e:
            print(e)
            return "admin not found"
        
    def no_users(self):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            user_data = cur.execute("SELECT * FROM user")
            return user_data
        except Exception as e:
            print(e)
            return "no user"
        
    def other_device_users(self):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            user_other_data = cur.execute("SELECT * FROM user_login")
            return user_other_data
        except Exception as e:
            print(e)
            return "no user"
    
    def no_admins(self):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            admin = cur.execute("SELECT * FROM admin")
            return admin
        except Exception as e:
            print(e)
            return "no admin"
        
    def slot_available(self):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM parking WHERE id=%s",(1,))
            data = cur.fetchone()
            slot = data['parking_available']
            return slot
        except Exception as e:
            print(e)
            return "no slot"