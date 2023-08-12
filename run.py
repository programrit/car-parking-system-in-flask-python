from flask import Flask,render_template,session
from user.login import Login
from user.signup import Signup
from user.dashboard import Dashboard
from admin.admin_login import AdminLogin
from datetime import timedelta
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from werkzeug.debug import DebuggedApplication
from waitress import serve



app = Flask(__name__,static_folder="C:/Users/Ram/Desktop/car-parking-system/static")
app.testing = True
my_app = DebuggedApplication(app,evalex=True, pin_security=True)
# serve(my_app,listen='*:500')
app.config.from_object('config_module.EmailConfig')
app.config.from_object('config_module.DatabaseConfig')
MySQL(app)
Bcrypt(app)
app.register_blueprint(Login.user_login)
app.register_blueprint(Signup.signup)
app.register_blueprint(Dashboard.dashboard)
app.register_blueprint(AdminLogin.admin_login)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('file_not_found.html',title="404")  
if __name__ == "__main__":
    app.run(debug=True)