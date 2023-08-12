from flask import Blueprint,render_template,redirect,session

from admin.libs import Library



library = Library()
class UserOtherTable:
    user_other_table = Blueprint('user_other_table',__name__,template_folder='templates')
    @user_other_table.route('/user-login-other-device')
    def user_other_data_table():
        try:
            admin = library.admin_exist()
            if 'admin_id' in session and 'login' in session and admin == "admin":
                return render_template('__user_other_device_table.html',title="User login Other Device")
            else:
                session.clear()
                return redirect('/admin-login', code=302)
        except:
            return render_template('404.html',title="404")
     