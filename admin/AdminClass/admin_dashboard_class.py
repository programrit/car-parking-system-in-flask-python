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