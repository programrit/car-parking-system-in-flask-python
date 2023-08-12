from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask import session,request
from user.mail_verify import email
import datetime

db = MySQL()

class UserFound:
    def __init__(self):
        pass
    
    def check_user_exist(self):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            user_id = session['id']
            cur.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
            check_user = cur.fetchone()
            if check_user:
                device = request.headers.get('User-Agent')
                get_device = check_user['device_info']
                if device == get_device:
                    return "user"
                else:
                    cur.execute("SELECT * FROM user_login WHERE user_id = %s AND device_info=%s", (user_id,device,))
                    check_user_database = cur.fetchone()
                    if check_user_database:
                        return "user"
                    else:
                        return "user not found"
            else:
                return "user not found"
        except Exception as e:
            return "user not found"
        
    def email_verify(self):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            user_id = session['id']
            cur.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
            verify = cur.fetchone()
            if verify['verify'] == 0:
                return "not verify"
            elif verify['verify'] == 1:
                return "verify"
            else:
                cur.execute('DELETE FROM user WHERE user_id=%s',(user_id,))
                db.connection.commit()
                cur.close()  
                return "signup"
        except Exception as e:
            
            return "something went wrong"
         
    def otp_verification(self,email_otp):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            user_id = session['id']
            cur.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
            otp_verify = cur.fetchone()
            date = otp_verify['date']
            otp = otp_verify['mail_otp']
            verify = otp_verify['verify']
            current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            date_format = datetime.datetime.strptime(str(date),"%Y-%m-%d %H:%M:%S")
            current_date_format = datetime.datetime.strptime(current_date,"%Y-%m-%d %H:%M:%S")
            date_time_different = current_date_format - date_format
            if verify == 1:
                return "alerady verify"
            else:
                if date_time_different.seconds > 900:
                    return "expired"
                else:
                    if otp != int(email_otp):
                        return "incorrect"
                    else:
                        cur.execute('UPDATE user SET verify=%s WHERE user_id =%s',(1,user_id,))
                        db.connection.commit()
                        cur.close()
                        return "verify"
        except Exception as e:
            
            return "otp verify failed"
        
    
    def resend_otp(self):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            user_id = session['id']
            cur.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
            fetch_gmail = cur.fetchone()
            gmail = fetch_gmail['email']
            mail = email(gmail)
            current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            get_value = mail.send_otp_email()
            mail_otp = get_value.split(",")[1]
            if "not send" == get_value:
                return "not send email"
            else:
                cur.execute('UPDATE user SET mail_otp=%s , date=%s WHERE user_id=%s AND email =%s',(mail_otp,current_date,user_id,gmail,))
                db.connection.commit()
                cur.close()
                return "otp send"
        except Exception as e:
            
            return "resend failed"