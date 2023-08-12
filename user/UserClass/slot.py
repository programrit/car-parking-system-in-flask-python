from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask import session,redirect
import datetime,random

db = MySQL()
class Slot:
    def __init__(self):
        pass
    def slot_update(self,slot_detail,slot_days):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM parking")
            slot_available_check = cur.fetchone()
            current_slot = slot_available_check['parking_available']
            if slot_detail == "book":
                update_slot = current_slot - int(slot_days)
                cur.execute('UPDATE parking SET parking_available=%s WHERE id=%s',(update_slot,1))
                db.connection.commit()
                cur.close()
                return "update"
            elif slot_detail == "cancel":
                update_slot = current_slot + int(slot_days)
                cur.execute('UPDATE parking SET parking_available=%s WHERE id=%s',(update_slot,1))
                db.connection.commit()
                cur.close()
                return "cancel"
            else:
                return "failed"
        except Exception as e:
            
            return "failed"

    def new_slot_booking(self,from_date,to_date,total,amount):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            user_id = session['id']
            cur.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
            get_id = cur.fetchone()
            if get_id:
                id = get_id['id']
                cur.execute("SELECT * FROM parking")
                slot_available_check = cur.fetchone()
                current_slot = slot_available_check['parking_available']
                if current_slot > 0:
                    try:
                        slot_id = "SLOT-"+datetime.datetime.now().isoformat(sep=" ",timespec="seconds").replace(':','').replace('-','').replace(' ','')+str(str(random.randint(99999,999999)))
                        payment_id = "PAY-ID-"+datetime.datetime.now().isoformat(sep=" ",timespec="seconds").replace(':','').replace('-','').replace(' ','')+str(str(random.randint(99999,999999)))
                        cur.execute("SELECT * FROM slot_booking WHERE user_id=%s",(id,))
                        slot_available = cur.fetchone()
                        if slot_available:
                            get_from = datetime.datetime.strptime(str(slot_available['from_date']),"%Y-%m-%d").date()
                            get_to = datetime.datetime.strptime(str(slot_available['to_date']),"%Y-%m-%d").date()
                            get_from_date = datetime.datetime.strptime(from_date,"%Y-%m-%d").date() 
                            get_to_date = datetime.datetime.strptime(to_date,"%Y-%m-%d").date() 
                            if get_from <= get_from_date <= get_to or get_from <= get_to_date <= get_to:
                                return "slot already booked"
                            else:
                                current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                cur.execute("INSERT INTO slot_booking (user_id,from_date,to_date,total_day,amount,booking_date,slot_id,payment_id,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(id,from_date,to_date,total,amount,current_date,slot_id,payment_id,"Payment Success",))
                                db.connection.commit()
                                cur.close()
                                if self.slot_update("book",total) == "update":
                                    return "booked"
                                else:
                                    return "failed"
                        else:
                            current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            cur.execute("INSERT INTO slot_booking (user_id,from_date,to_date,total_day,amount,booking_date,slot_id,payment_id,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(id,from_date,to_date,total,amount,current_date,slot_id,payment_id,"Payment Success",))
                            db.connection.commit()
                            cur.close()
                            if self.slot_update("book",total) == "update":
                                return "booked"
                            else:
                                return "failed"
                    except Exception as e:
                        
                        return "failed"
                else:
                    return "not avilable"
            else:
                return redirect('/user-login',code=302)
        except Exception as e:
            
            return "failed"
        
    
    def slot_cancel(self,id):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            user_id = session['id']
            cur.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
            get_id = cur.fetchone()
            if get_id:
                get_user_id = get_id['id']
                cur.execute("SELECT * FROM slot_booking WHERE user_id=%s AND id=%s",(get_user_id,id))
                slot_available = cur.fetchone()
                day = slot_available['total_day']
                if slot_available:
                    if self.slot_update("cancel",day) == "cancel":
                        cur.execute('DELETE FROM slot_booking WHERE user_id=%s AND id=%s',(get_user_id,id))
                        db.connection.commit()
                        cur.close()  
                        return "delete"
                    else:
                        return "failed"
                else:
                    return "slot not found"

        except Exception as e:
            
            return "failed"
        

    def show_slot_data(self):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            user_id = session['id']
            cur.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
            get_id = cur.fetchone()
            if get_id:
                id = get_id['id']
                cur.execute("SELECT * FROM slot_booking WHERE user_id=%s",(id,))
                slot_available = cur.fetchall()
                if slot_available:
                    return slot_available
                else:
                    return "no slot"
            else:
                return redirect('/user-login',code=302)
        except Exception as e:
            
            return "no slot"

    def no_of_slot_available(self):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM parking")
            slot_available_check = cur.fetchone()
            if slot_available_check:
                current_slot = slot_available_check['parking_available']
                return current_slot
            else:
                return "no"
        except Exception as e:
            
            return "no"
        

    def print_slot(self,id):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            user_id = session['id']
            cur.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
            fetch_data= cur.fetchone()
            if fetch_data:
                cur.execute("SELECT * FROM slot_booking WHERE id=%s",(id,))
                slot = cur.fetchone()
                if slot:
                    slot['name'] = fetch_data['name']
                    return slot
                else:
                    return "failed"
            else:
                return "failed"
        except Exception as e:
            
            return "failed"