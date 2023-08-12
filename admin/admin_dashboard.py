from flask import Blueprint,render_template,redirect,session

from admin.libs import Library



library = Library()
class AdminDashboard:
    admin_dashboard = Blueprint('admin_dashboard',__name__,template_folder='templates')
    @admin_dashboard.route('/admin-dashboard')
    def dashboard():
        try:
            admin = library.admin_exist()
            if 'admin_id' in session and 'login' in session and admin == "admin":
                return render_template('__admin_dashboard.html',title="Admin Dashboard")
            else:
                session.clear()
                return redirect('/admin-login', code=302)
        except:
            return render_template('404.html',title="404")
     