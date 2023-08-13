from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask import session,request
from flask_bcrypt import Bcrypt 
from user.mail_verify import email
from user.UserClass.check_user import UserFound
import os

bcrypt = Bcrypt()
db = MySQL()
class UserLogin:
    def __init__(self):
        pass

    def user_login(self,gmail,password):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM user WHERE email = %s", (gmail,))
            email_exist = cur.fetchone()
            user_id = email_exist['user_id']
            session.permanent = True
            if email_exist:
                session['id'] = user_id
                if email_exist['verify'] == 1:
                    get_password = email_exist['password']
                    check_password = bcrypt.check_password_hash(get_password,password)
                    if check_password:
                        current_device_info = request.headers.get('User-Agent')
                        device_info  = email_exist['device_info']
                        if device_info:
                            if device_info == current_device_info:
                                return "login"
                            else:
                                send_user = email(gmail)
                                send = send_user.send_email_user(current_device_info)
                                if send == "send":
                                    cur.execute("SELECT * FROM user_login WHERE user_id = %s AND device_info=%s", (user_id,current_device_info,))
                                    check_user_login = cur.fetchone()
                                    if check_user_login:
                                        return "login"
                                    else:
                                        id = email_exist['id']
                                        cur.execute("INSERT INTO user_login (user_main_id,user_id,device_info) VALUES (%s,%s,%s)",(id,user_id,current_device_info))
                                        db.connection.commit()
                                        cur.close()
                                        return "login"
                                else:
                                    return "failed"
                        else:
                            update = UserFound.resend_otp()
                            if update == "not send email":
                               return "not send email"
                            elif update == "otp send":
                                return "not verify"
                            else:
                                return "failed"
                    else:
                        return "password incorrect"
                else:
                    update = UserFound.resend_otp()
                    if update == "not send email":
                       return "not send email"
                    elif update == "otp send":
                        return "not verify"
                    else:
                        return "failed"
                   
            else:
                return "email not found"
        except Exception as e:
            return "login failed"
        
    
    def share_user_data(self):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            user_id = session['id']
            cur.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
            check_user = cur.fetchone()
            if check_user:
                return check_user
            else:
                return "user not found"
        except Exception as e:
            
            return "user not found"
        

    def update_user(self,name,email,phone,profile):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            user_id = session['id']
            if profile == "empty":
                cur.execute('UPDATE user SET name=%s , email=%s , phone_no=%s WHERE user_id=%s',(name,email,phone,user_id,))
                db.connection.commit()
                cur.close()
                return "update"
            else:
                cur.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
                check_profile = cur.fetchone()
                print(check_profile['profile'])
                if check_profile['profile'] == "" or check_profile['profile'] ==None:
                    cur.execute('UPDATE user SET name=%s , email=%s , phone_no=%s, profile=%s WHERE user_id=%s',(name,email,phone,profile,user_id,))
                    db.connection.commit()
                    cur.close()
                    return "update"
                else:
                    try:
                        os.remove(os.path.join("C:/Users/Ram/Desktop/test/static/user_profile/",check_profile['profile']))
                        cur.execute('UPDATE user SET name=%s , email=%s , phone_no=%s, profile=%s WHERE user_id=%s',(name,email,phone,profile,user_id,))
                        db.connection.commit()
                        cur.close()
                        return "update"
                    except Exception as e:
                        
                        return "update failed"

        except Exception as e:
            
            return "update failed"

    def logout(self):
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
                    get_data = cur.fetchone()
                    if get_data:
                        cur.execute('DELETE FROM user_login WHERE user_id=%s',(user_id,))
                        db.connection.commit()
                        cur.close()  
                        return "logout"
                    else:
                        return "logout"
                else:
                    cur.execute("SELECT * FROM user_login WHERE user_id = %s", (user_id,))
                    get_data_1 = cur.fetchone()
                    if get_data_1:
                        cur.execute('DELETE FROM user_login WHERE user_id=%s',(user_id,))
                        db.connection.commit()
                        cur.close()  
                        return "logout"
                    else:
                        return "logout"
        except Exception as e:
            
            return "failed"
        