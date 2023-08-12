from flask import Blueprint,render_template,redirect,session

from admin.libs import Library



library = Library()
class AdminTable:
    admin_table = Blueprint('admin_table',__name__,template_folder='templates')
    @admin_table.route('/admin-table')
    def admin_table_data():
        try:
            admin = library.admin_exist()
            if 'admin_id' in session and 'login' in session and admin == "admin":
                return render_template('__admin_table.html',title="Admin Table")
            else:
                session.clear()
                return redirect('/admin-login', code=302)
        except:
            return render_template('404.html',title="404")
     