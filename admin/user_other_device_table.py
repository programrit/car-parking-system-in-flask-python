from flask import Blueprint,render_template,redirect,session,request
from admin.libs import Library

library = Library()
class UserOtherTable:
    user_other_table = Blueprint('user_other_table',__name__,template_folder='templates')
    @user_other_table.route('/user-login-other-device')
    def user_other_data_table():
        try:
            admin = library.admin_exist()
            if 'admin_id' in session and 'login' in session and admin == "admin":
                other_device_data = library.other_device_user_data()
                current_admin_data = library.current_admin_data()
                if other_device_data !="no users":
                    return render_template('__user_other_device_table.html',title="User login Other Device",other_device_data = other_device_data,current_admin_data=current_admin_data)
                else:
                    return render_template('__user_other_device_table.html',title="User login Other Device",current_admin_data=current_admin_data)
            else:
                session.clear()
                return redirect('/admin-login', code=302)
        except:
            return render_template('404.html',title="404")

    @user_other_table.route('/user-login-other-device',methods=['POST','GET'])
    def delete_other_user_data():
        if request.method == 'GET':
            return redirect('/user-login-other-device',code=302)
        elif request.method =='POST':
            if request.form.get('other_user_id'):
                other_user_id = request.form.get('other_user_id')
                delete = library.delete_other_user_data(other_user_id)
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
     