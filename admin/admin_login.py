from flask import Blueprint,render_template,request,url_for,redirect,session
import string,random
from admin.libs import Library
from flask_bcrypt import Bcrypt


library = Library()
class AdminLogin:
    admin_login = Blueprint('admin_login',__name__,template_folder='templates')
    @admin_login.route('/admin-login')
    def login_admin():
        try:
            admin = library.admin_exist()
            if 'admin_id' in session and 'login' in session and admin == "admin":
                return redirect('/admin-dashboard', code=302)
            else:
                no_captcha = 6
                captcha = "".join(random.choices(string.ascii_uppercase+string.digits,k=no_captcha))
                return render_template('__admin_login.html',title="Admin Login",captcha = captcha)
        except:
            return render_template('404.html',title="404")
        
    @admin_login.route('/admin-login',methods=['POST','GET'])
    def admin_login_data():
        if request.method =="GET":
            return redirect(url_for("login_admin"))
        elif request.method=="POST":
            if 'refresh' in request.form:
                no_captcha = 6
                captcha = "".join(random.choices(string.ascii_uppercase+string.digits,k=no_captcha))
                return captcha
            elif request.form.get('email') and request.form.get('password'):
                email = request.form.get('email')
                password = request.form.get('password')
                user=library.admin_login_verification(email,password)
                if user == "login":
                    session['login'] = True
                    session.permanent = True
                    return "login"
                elif user == "password incorrect":
                    return "Please enter correct password"
                elif user == "login failed":
                    return "Email not found. Please enter correct email or signup"
                elif user == "email not found":
                    return "Please enter correct email or new user please signup"
                elif user == "not send email":
                    return "not send email"
                else:
                    return "Something went wrong. Please try agin later"
            else:
                return render_template('404.html',title="404")
        else:
            return render_template('404.html',title="404")