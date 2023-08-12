from flask import Blueprint,render_template,request,url_for,redirect,session
import string,random
from user.libs import Library
from flask_bcrypt import Bcrypt


library = Library()
bcrypt = Bcrypt()
class Login:
    user_login = Blueprint('user_login',__name__,template_folder='templates')
    @user_login.route('/user-login')
    def login_user():
        try:
            user = library.check_user()
            if 'id' in session and 'login' in session and user=="user":
                return redirect('/',code=302)
            else:
                no_captcha = 6
                captcha = "".join(random.choices(string.ascii_uppercase+string.digits,k=no_captcha))
                return render_template('user_login.html',title="Login",captcha=captcha)
        except:
            return render_template('file_not_found.html',title="404")
        
    @user_login.route('/user-login',methods=['GET','POST'])
    def user_login_data():
        if request.method =="GET":
            return redirect(url_for("login_user"))
        elif request.method=="POST":
            if 'refresh' in request.form:
                no_captcha = 6
                captcha = "".join(random.choices(string.ascii_uppercase+string.digits,k=no_captcha))
                return captcha
            elif request.form.get('email') and request.form.get('password'):
                email = request.form.get('email')
                password = request.form.get('password')
                user=library.login(email,password)
                if user == "login":
                    session['login'] = True
                    session.permanent = True
                    return "login"
                elif user == "password incorrect":
                    return "Please enter correct password"
                elif user == "login failed":
                    return "Email not found. Please enter correct email or signup"
                elif user == "not verify":
                    return "not verify"
                elif user == "email not found":
                    return "Please enter correct email or new user please signup"
                elif user == "not send email":
                    return "not send email"
                else:
                    return "Something went wrong. Please try agin later"
            else:
                return render_template('file_not_found.html',title="404")
        else:
            return render_template('file_not_found.html',title="404")

    @user_login.route('/user-login/forget-password')
    def forget_passoword():
        try:
            return render_template("forget_password.html",title="Forget Password")
        except:
            return render_template('file_not_found.html',title="404")

    @user_login.route('/user-login/forget-password',methods=['POST','GET'])
    def passoword():
        if request.method == 'GET':
            return redirect(url_for("forget_passoword"))
        elif request.method == 'POST':
            if request.form.get('email'):
                email = request.form.get('email')
                send_otp = library.forget_password(email)
                if send_otp == "update":
                    return "send"
                elif send_otp == "user not found":
                    return "User not found. Please enter correct email or signup"
                elif send_otp == "not send email":
                    return "OTP send failed. Please try again later"
                else:
                    return "Something went wrong"
        else:
            return render_template('file_not_found.html',title="404")
        
    @user_login.route('/user-login/email-verification')
    def email_phone_verify():
        try:
            user = library.check_user()
            if 'id' in session and 'login' in session and user=="user":
                return redirect('/',code=302)
            else:
                verify = library.account_verify()
                if session['id'] and verify == "not verify":
                    return render_template('email_verify.html',title= "OTP Verification")
                else:
                    return redirect('/user-login',code=302)
        except:
            return render_template('file_not_found.html',title="404")


    @user_login.route('/user-login/email-verification',methods=['POST','GET'])
    def resend_otp():
            if request.method == 'GET':
               return redirect(url_for('email_phone_verify'))
            elif request.method == 'POST':
                if request.form.get('resend_otp_email'):
                    account_verify = library.account_verify()
                    if account_verify == "not verify":
                        resend_otp = library.otp_update()
                        if resend_otp == "otp send":
                            return "otp send"
                        elif resend_otp == "not send email":
                            return "otp not send"
                        else:
                            return "something went wrong"
                    else:
                        return redirect('/user-login',code=302)
                elif request.form.get('email_otp'):
                    email_otp = request.form.get('email_otp')
                    check = library.check_otp_forget(email_otp)
                    if check =="expired":
                        return "otp expired"
                    elif check == "incorrect":
                        return "incorrect otp"
                    elif check == "verify":
                        return "OTP verfication successfully"
                    elif check == "otp verify failed":
                        return "otp verify failed"
                    elif check == "alerady verify":
                        return "alerady verify"
                    else:
                        return "Something went wrong"
                
                else:
                    return render_template('file_not_found.html',title="404")
            else:
                return render_template('file_not_found.html',title="404")

    @user_login.route('/user-login/change-password')
    def change_password():
        try:
            check = library.check_new_password()
            if check == "allowed" and 'id' in session:
                return render_template("new_password.html",title="New Password")
            else:
                return redirect('/user-login',code=302)
        except:
            return render_template('file_not_found.html',title="404")
        

    @user_login.route('/user-login/change-password', methods= ['POST','GET'])
    def update_password():
        if request.method == 'GET':
            return redirect(url_for('change_password'))
        elif request.method == 'POST':
            if request.form.get('new_password') and request.form.get('confirm_password'):
                new_password = request.form.get('new_password')
                confirm_password = request.form.get('confirm_password')
                hash_new_password = bcrypt.generate_password_hash(new_password).decode("utf-8")
                hash_confirm_password = bcrypt.generate_password_hash(confirm_password).decode("utf-8")
                update = library.update_password(hash_new_password,hash_confirm_password)
                if update == "update":
                    return "update"
                else:
                    return "Password update failed. Please try again"
        else:
            return render_template('file_not_found.html',title="404")
    



        
        


        
    
