from flask import Blueprint,render_template,request,url_for,redirect,session
import string,random
from admin.libs import Library
from flask_bcrypt import Bcrypt



library = Library()
bcrypt = Bcrypt()

class AdminLogin:
    admin_login = Blueprint('user_login',__name__,template_folder='templates')
    @admin_login.route('/admin-login')
    def login_admin():
        try:
            return render_template('__admin_login.html',title="Admin Login",)
        except Exception as e:
            return render_template('file_not_found.html',title="404")