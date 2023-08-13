from flask import Blueprint,render_template,redirect,session,request

from admin.libs import Library



library = Library()
class AdminOtherTable:
    admin_other_table = Blueprint('admin_other_table',__name__,template_folder='templates')
    @admin_other_table.route('/admin-login-other-device')
    def admin_other_table_data():
        try:
            admin = library.admin_exist()
            if 'admin_id' in session and 'login' in session and admin == "admin":
                other_device_admin = library.other_device_admin_data()
                if other_device_admin != "no admin":
                    return render_template('__admin_other_device_table.html',title="User Table",other_device_admin=other_device_admin)
                else:
                    return render_template('__admin_other_device_table.html',title="User Table")
            else:
                session.clear()
                return redirect('/admin-login', code=302)
        except:
            return render_template('404.html',title="404")
        
    @admin_other_table.route('/admin-login-other-device',methods=['POST','GET'])
    def delete_other_admin_data():
        if request.method == 'GET':
            return redirect('/admin-login-other-device',code=302)
        elif request.method =='POST':
            if request.form.get('other_admin_id'):
                other_admin_id = request.form.get('other_admin_id')
                delete = library.delete_other_admin_data(other_admin_id)
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
    
     