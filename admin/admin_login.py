from flask import Blueprint,render_template,request,url_for,redirect,session
import string,random
from user.libs import Library
from flask_bcrypt import Bcrypt


class AdminLogin:
    admin_login = Blueprint('admin_login',__name__,template_folder='templates')
    @admin_login.route('/admin-login')
    def login_admin():
        try:
            return render_template('__admin_login.html',title="Admin Login")
        except:
            return render_template('file_not_found.html',title="404")