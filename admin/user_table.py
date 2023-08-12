from flask import Blueprint,render_template,redirect,session

from admin.libs import Library



library = Library()
class UserTable:
    user_table = Blueprint('user_table',__name__,template_folder='templates')
    @user_table.route('/user-table')
    def user_table_data():
        try:
            admin = library.admin_exist()
            if 'admin_id' in session and 'login' in session and admin == "admin":
                return render_template('__user_table.html',title="User Table")
            else:
                session.clear()
                return redirect('/admin-login', code=302)
        except:
            return render_template('404.html',title="404")
     