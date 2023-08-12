from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask import session
from flask_bcrypt import Bcrypt 
from user.mail_verify import email
import datetime

bcrypt = Bcrypt()
db = MySQL()
class PasswordUpdate:
    def __init__(self):
       pass

    def update_password(self,old_password,new_password,confirm_password):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            user_id = session['id']
            cur.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
            get_data= cur.fetchone()
            if get_data:
                get_password = get_data['password']
                if bcrypt.check_password_hash(get_password,old_password):
                    cur.execute('UPDATE user SET password=%s, confirm_password=%s WHERE user_id=%s',(new_password,confirm_password,user_id))
                    db.connection.commit()
                    cur.close()
                    return "update"
                else:
                    return "incorrect password"
            else:
                return "failed"
        except Exception as e:
            
            return "failed"
    
    def forget_password_in_user(self,gmail):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM user WHERE email = %s", (gmail,))
            get_email= cur.fetchone()
            if get_email:
                mail = email(gmail)
                get_value = mail.send_otp_email()
                mail_otp = get_value.split(",")[1]
                if "not send" == get_value:
                    return "not send email"
                else:
                    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    user_id = get_email['user_id']
                    session['id'] = user_id
                    session.permanent = True
                    cur.execute('UPDATE user SET mail_otp=%s, date=%s, verify=%s WHERE user_id=%s AND email=%s',(mail_otp,current_date,0,user_id,gmail,))
                    db.connection.commit()
                    cur.close()
                    return "update"
            else:
                return "user not found"
        except Exception as e:
            
            return "otp send failed"
        
    def otp_send_for_forget_password(self,email_otp):
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
                        cur.execute('UPDATE user SET verify=%s, change_password=%s, change_password_date=%s WHERE user_id =%s',(1,1,current_date,user_id,))
                        db.connection.commit()
                        cur.close()
                        return "verify"
        except Exception as e:
            
            return "otp verify failed"
        

    def update_new_password_time_validation(self):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            user_id = session['id']
            cur.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
            otp_verify = cur.fetchone()
            date = otp_verify['change_password_date']
            if date:
                verify = otp_verify['change_password']
                current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                date_format = datetime.datetime.strptime(str(date),"%Y-%m-%d %H:%M:%S")
                current_date_format = datetime.datetime.strptime(current_date,"%Y-%m-%d %H:%M:%S")
                date_time_different = current_date_format - date_format
                if verify == 1:
                    if date_time_different.seconds > 1800:
                        cur.execute('UPDATE user SET change_password=%s, change_password_date=%s WHERE user_id =%s',(0,"",user_id,))
                        db.connection.commit()
                        cur.close()
                        return "not allowed"
                    else:
                        return "allowed"
                else:
                    cur.execute('UPDATE user SET change_password=%s, change_password_date=%s WHERE user_id =%s',(0,"",user_id,))
                    db.connection.commit()
                    cur.close()
                    return "not allowed"
            else:
                cur.execute('UPDATE user SET change_password=%s, change_password_date=%s WHERE user_id =%s',(0,"",user_id,))
                db.connection.commit()
                cur.close()
                return "not allowed"
        except Exception as e:
            
            return "not allowed"
        
    
    def password_update_database(self,new_password,confirm_password):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            user_id = session['id']
            cur.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
            get_data= cur.fetchone()
            if get_data:
                cur.execute('UPDATE user SET password=%s, confirm_password=%s, change_password=%s, change_password_date=%s WHERE user_id=%s',(new_password,confirm_password,0,"",user_id))
                db.connection.commit()
                cur.close()
                return "update"
            else:
                return "failed"
        except Exception as e:
            
            return "failed"
