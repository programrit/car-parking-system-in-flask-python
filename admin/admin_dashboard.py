from flask import Blueprint,render_template,redirect,session,request

from admin.libs import Library



library = Library()
class AdminDashboard:
    admin_dashboard = Blueprint('admin_dashboard',__name__,template_folder='templates')
    @admin_dashboard.route('/admin-dashboard')
    def dashboard():
        try:
            admin = library.admin_exist()
            if 'admin_id' in session and 'login' in session and admin == "admin":
                users = library.no_user()
                other_users = library.other_device_user()
                admin_data = library.admin()
                slot = library.no_slot()
                current_admin_data = library.current_admin_data()
                return render_template('__admin_dashboard.html',title="Admin Dashboard",users=users,other_users=other_users,admin_data=admin_data,slot=slot,current_admin_data=current_admin_data)
            else:
                session.clear()
                return redirect('/admin-login', code=302)
        except:
            return render_template('404.html',title="404")
        
    @admin_dashboard.route('/logout', methods=['POST','GET'])
    def logout():
        if request.method == 'POST':
            if request.form.get('logout'):
                logout = library.logout_user()
                if logout == "logout":
                    session.clear()
                    return "logout"
                else:
                    return "User not found"
        elif request.method == 'GET':
            return render_template('404.html',title="404")
        else:
            return render_template('404.html',title="404")

     