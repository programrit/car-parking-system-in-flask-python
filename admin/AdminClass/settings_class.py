from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask import session,request
from user.mail_verify import email
from flask_bcrypt import Bcrypt


db = MySQL()
bcrypt = Bcrypt()

class SettingChangePassword:
    def __init__(self):
        pass

    def delete_other_account_password(self):
        try:
            admin_id = session['admin_id']
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM admin_login WHERE admin_id=%s",(admin_id,))
            admin_other_data = cur.fetchone()
            if admin_other_data:
                cur.execute("DELETE FROM admin_login WHERE admin_id=%s",(admin_id,))
                db.connection.commit()
                cur.close()
                return "delete"
            else:
                return "no user"
        except Exception as e:
            print(e)
            return "no user"
    
    def change_password_settings(self,old_password,new_password):
        try:
            admin_id = session['admin_id']
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM admin WHERE admin_id=%s",(admin_id,))
            admin_data = cur.fetchone()
            if admin_data:
                get_password =admin_data['password']
                check_password = bcrypt.check_password_hash(get_password,old_password)
                if check_password:
                    if old_password == new_password:
                        return "same password"
                    else:
                        hash_new_password = bcrypt.generate_password_hash(new_password).decode("utf-8")
                        cur.execute("UPDATE admin SET password=%s WHERE admin_id=%s",(hash_new_password,admin_id,))
                        db.connection.commit()
                        cur.close()
                        return "update"
                else:
                    return "wrong password"
            else:
                return "no users"
        except Exception as e:
            print(e)
            return "failed"
        
    