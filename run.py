from flask import Flask,render_template,session
from user.login import Login
from user.signup import Signup
from user.dashboard import Dashboard
from datetime import timedelta
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from werkzeug.debug import DebuggedApplication
from waitress import serve

from admin.admin_login import AdminLogin
from admin.admin_dashboard import AdminDashboard
from admin.user_table import UserTable
from admin.user_other_device_table import UserOtherTable
from admin.slot_booking import UserSlotBooking
from admin.admin_table import AdminTable
from admin.admin_other_device_table import AdminOtherTable
from admin.settings import Settings
from flask_wtf import CSRFProtect

app = Flask(__name__,static_folder="C:/Users/Ram/Desktop/car-parking-system/static")
app.testing = True
my_app = DebuggedApplication(app,evalex=True, pin_security=True)
# serve(my_app,listen='*:500')
app.config.from_object('config_module.Config')
app.config.from_object('config_module.EmailConfig')
app.config.from_object('config_module.DatabaseConfig')
MySQL(app)
Bcrypt(app)
CSRFProtect(app)
app.register_blueprint(Login.user_login)
app.register_blueprint(Signup.signup)
app.register_blueprint(Dashboard.dashboard)
app.register_blueprint(AdminLogin.admin_login)
app.register_blueprint(AdminDashboard.admin_dashboard)
app.register_blueprint(UserTable.user_table)
app.register_blueprint(UserOtherTable.user_other_table)
app.register_blueprint(UserSlotBooking.slot_booking)
app.register_blueprint(AdminTable.admin_table)
app.register_blueprint(AdminOtherTable.admin_other_table)
app.register_blueprint(Settings.setting)

@app.errorhandler(404)
def page_not_found(e):
    if 'admin_id' in session and 'login' in session:
        return render_template('404.html',title="404")  
    elif 'id' in session and 'login' in session:
        return render_template('file_not_found.html',title="404")
    else:
        return render_template('file_not_found.html',title="404")
if __name__ == "__main__":
    app.run(debug=True)