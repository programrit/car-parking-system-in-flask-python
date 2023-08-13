from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask import session,request
from flask_bcrypt import Bcrypt 
from user.mail_verify import email


bcrypt = Bcrypt()
db = MySQL()

class AdminLoginVerify:
    def __init__(self):
        pass

    def login(self,gmail,password):
        try:
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM admin WHERE email = %s", (gmail,))
            email_exist = cur.fetchone()
            admin_id = email_exist['admin_id']
            session.permanent = True
            if email_exist:
                session['admin_id'] = admin_id
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
                                cur.execute("SELECT * FROM admin_login WHERE user_id = %s AND device_info=%s", (admin_id,current_device_info,))
                                check_user_login = cur.fetchone()
                                if check_user_login:
                                    return "login"
                                else:
                                    id = email_exist['id']
                                    cur.execute("INSERT INTO admin_login (admin_main_id,admin_id,device_info) VALUES (%s,%s,%s)",(id,admin_id,current_device_info))
                                    db.connection.commit()
                                    cur.close()
                                    return "login"
                            else:
                                cur.execute("SELECT * FROM admin_login WHERE user_id = %s AND device_info=%s", (admin_id,current_device_info,))
                                check_user_login_1 = cur.fetchone()
                                if check_user_login_1:
                                    return "login"
                                else:
                                    get_id = email_exist['id']
                                    cur.execute("INSERT INTO admin_login (admin_main_id,admin_id,device_info) VALUES (%s,%s,%s)",(get_id,admin_id,current_device_info))
                                    db.connection.commit()
                                    cur.close()
                                    return "login"
                    else:
                        cur.execute("UPDATE admin SET device_info=%s WHERE email=%s",(current_device_info,gmail))
                        db.connection.commit()
                        cur.close()
                        return "login"
                else:
                    return "password incorrect"
                   
            else:
                return "email not found"
        except Exception as e:
            print(e)
            return "login failed"
