from flask import Blueprint,render_template,redirect,session,request
from admin.libs import Library
import math,random


library = Library()
class Settings:
    setting = Blueprint('settings',__name__,template_folder='templates')
    @setting.route('/settings')
    def change_password():
        try:
            admin = library.admin_exist()
            if 'admin_id' in session and 'login' in session and admin == "admin":
                admin = library.admin_data()
                current_admin_data = library.current_admin_data()
                return render_template('__settings.html',title="Change Password",current_admin_data=current_admin_data)
            else:
                session.clear()
                return redirect('/admin-login', code=302)
        except Exception as e:
            return render_template('404.html',title="404")
        
    
    @setting.route('/settings', methods=['POST','GET'])
    def change_password_setting():
        if request.method == 'GET':
            return redirect('/settings',code=302)
        elif  request.method == 'POST':
            try:
                old_password = request.form.get('old_password')
                new_password = request.form.get('new_password')
                password = library.change_password(old_password,new_password)
                if password == "update":
                    return "update"
                elif password == "wrong password":
                    return "Please enter correct old password"
                elif password == "same password":
                    return "Old password is same new password. Please enter different password"
                elif password == "failed":
                    return "Password update failed"
                elif password == "no users":
                    return "User not found"
                else:
                    return "Something went wrong"
            except Exception as e:
                return render_template('404.html',title="404")
            
        else:
            return render_template('404.html',title="404")