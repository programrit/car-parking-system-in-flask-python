from flask import Blueprint,render_template,redirect,session,request
from flask_bcrypt import Bcrypt
from admin.libs import Library
import math,random,datetime


library = Library()
bcrypt = Bcrypt()
class UserTable:
    user_table = Blueprint('user_table',__name__,template_folder='templates')
    @user_table.route('/user-table')
    def user_table_data():
        try:
            admin = library.admin_exist()
            if 'admin_id' in session and 'login' in session and admin == "admin":
                user_data = library.user_data()
                current_admin_data = library.current_admin_data()
                if user_data != "no users":
                    return render_template('__user_table.html',title="User Table",user_data=user_data,current_admin_data=current_admin_data)
                else:
                    return render_template('__user_table.html',title="User Table",current_admin_data=current_admin_data)
            else:
                session.clear()
                return redirect('/admin-login', code=302)
        except:
            return render_template('404.html',title="404")
        
    @user_table.route('/user-table', methods=['POST','GET'])
    def user_table_add():
        if request.method == 'GET':
            return redirect('/user-table',code=302)
        elif request.method == 'POST':
            if request.form.get('name') and request.form.get("email") and request.form.get("phone") and request.form.get("confirm_password"): 
                name = request.form.get("name")
                gmail = request.form.get("email")
                mobile = request.form.get("phone")
                password = request.form.get("password")
                password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
                confirm_password = request.form.get("confirm_password")
                confirm_password_hash = bcrypt.generate_password_hash(confirm_password).decode('utf-8')
                digits = "0123456789"
                first_random =""
                second_random=""
                count = 5
                phone = str(mobile)
                no =""
                for i in range(7):
                    first_random+=digits[math.floor(random.random()*10)]
                for i in range(7):
                    second_random+=digits[math.floor(random.random()*10)]
                while (count>0):
                    no+=phone[-count]
                    count=count-1
                user_id = "USER_"+first_random+no+second_random
                add = library.add_new_user(user_id,name,mobile,gmail,password_hash,confirm_password_hash)
                if add == "add":
                    return "add"
                elif add == "not add":
                    return "Data add failed"
                elif add =="email exist":
                    return "Email already exist"
                elif add == "phone exist":
                    return "Phone no already exist"
                else:
                    return "Something went wrong"
                
            elif request.form.get('id'):
                user_id = request.form.get('id')
                data  = library.show_update_data(user_id)
                if data == "no user":
                    return "no user"
                else:
                    return data
                  
            elif request.form.get('user_id') and request.form.get('name'):
                name = request.form.get("name")
                user_id = request.form.get('user_id')
                update = library.update_user_data(user_id,name)
                if update == "update":
                    return "update"
                elif update=="failed":
                    return "Update failed. Please try again later"
                else:
                    return "Something went wrong"
                
            elif request.form.get('delete_id'):
                delete_id = request.form.get('delete_id')
                delete = library.delete_user_data(delete_id)
                if delete == "delete":
                    return "delete"
                elif delete == "failed":
                    return "User data delete failed. Please try again later"
                else:
                    return "Something went wrong"
            else:
                return render_template('404.html',title="404")
        else:
            return render_template('404.html',title="404")
     