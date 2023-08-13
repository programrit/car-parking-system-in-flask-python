from user.mail_verify import email
from flask import request,session
from flask_mysqldb import MySQL
import MySQLdb.cursors

db = MySQL()
class NewUser:
    def __init__(self):
        pass

    # insert new user data in database    
    def insert(self,user_id,name,mobile,gmail,password,confirm_password,mail_otp,date):
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
                    mail = email(gmail)
                    get_value = mail.send_otp_email()
                    mail_otp = get_value.split(",")[1]
                    if "not send" == get_value:
                        return "not send email"
                    else:
                        device_info = request.headers.get('User-Agent')
                        cur.execute("INSERT INTO user (user_id,name,phone_no,email,password,confirm_password,mail_otp,date,device_info) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(user_id,name,mobile,gmail,password,confirm_password,mail_otp,date,device_info,))
                        db.connection.commit()
                        cur.close()
                        return "inserted"
        except Exception as e:
            return "not insert"
        
    
    def notification_show(self):
        try:
           cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
           user_id = session['id']
           cur.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
           current_data = cur.fetchone()
           if current_data:
               device_info = current_data['device_info']
               device = request.headers.get('User-Agent')
               if device == device_info:
                   cur.execute("SELECT * FROM user_login WHERE user_id = %s", (user_id,))
                   get_data = cur.fetchall()
                   if get_data:
                        notification = get_data
                        return notification
                   else:
                       return "null"
               else:
                   return "null"
        except Exception as e:
            
            return "null"
        

