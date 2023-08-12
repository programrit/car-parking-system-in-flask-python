from flask_mysqldb import MySQL
import MySQLdb.cursors
import datetime

db = MySQL()

class Contact:
    def __init__(self):
        pass

    def contact_team(self,contact_name,contact_email,contact_phone,contact_message):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM contact WHERE email = %s", (contact_email,))
            email_exist = cur.fetchone()
            if email_exist:
                return "exist"
            else:
                cur.execute("SELECT * FROM contact WHERE phone = %s", (contact_phone,))
                phone_exist = cur.fetchone()
                if phone_exist:
                    return "exist"
                else:
                    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    cur.execute("INSERT INTO contact (name,email,phone,message,date) VALUES (%s,%s,%s,%s,%s)",(contact_name,contact_email,contact_phone,contact_message,current_date))
                    db.connection.commit()
                    cur.close()
                    return "inserted"
        except Exception as e:
            
            return "failed"