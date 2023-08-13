from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask import session,request
from user.mail_verify import email


db = MySQL()

class SlotBookingTable:
    def __init__(self):
        pass

    def user_slot_booking(self):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM slot_booking")
            slot_data = cur.fetchall()
            if slot_data:
                return slot_data
            else:
                return "no slot"
        except Exception as e:
            print(e)
            return "no slot"
        
    
    def delete_user_slot_in_admin(self,slot_id):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM slot_booking WHERE id=%s",(slot_id,))
            slot_data = cur.fetchone()
            if slot_data:
                cur.execute("DELETE FROM slot_booking WHERE id=%s",(slot_id,))
                db.connection.commit()
                cur.close()
                return "delete"
            else:
                return "failed"
        except Exception as e:
            print(e)
            return "failed"