from flask import Blueprint,render_template,redirect,session,request
from admin.libs import Library
import math,random


library = Library()
class AdminTable:
    admin_table = Blueprint('admin_table',__name__,template_folder='templates')
    @admin_table.route('/admin-table')
    def admin_table_data():
        try:
            admin = library.admin_exist()
            if 'admin_id' in session and 'login' in session and admin == "admin":
                admin = library.admin_data()
                if admin != "no admin":
                    return render_template('__admin_table.html',title="Admin Table",admin=admin)
                else:
                    return render_template('__admin_table.html',title="Admin Table")
            else:
                session.clear()
                return redirect('/admin-login', code=302)
        except:
            return render_template('404.html',title="404")
        
    
    @admin_table.route('/admin-table', methods=['POST','GET'])
    def admin_table_add():
        if request.method == 'GET':
            return redirect('/user-table',code=302)
        elif request.method == 'POST':
            if request.form.get("name") and request.form.get("email") and request.form.get("password"):
                name = request.form.get("name")
                gmail = request.form.get("email")
                password = request.form.get("password")
                digits = "0123456789"
                first_random =""
                second_random=""
                for i in range(7):
                    first_random+=digits[math.floor(random.random()*10)]
                for i in range(7):
                    second_random+=digits[math.floor(random.random()*10)]
                user_id = "USER_"+first_random+second_random
                add = library.add_new_admin(user_id,name,gmail,password)
                if add == "add":
                    return "add"
                elif add == "not add":
                    return "Data add failed"
                elif add =="email exist":
                    return "Email already exist"
                elif add == "not send":
                    return "Password send your failed. Please check your internet connection or contact admin"
                else:
                    return "Something went wrong"
            elif request.form.get('admin_id'):
                admin_id = request.form.get('admin_id')
                delete = library.delete_admin_data(admin_id)
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
    
     