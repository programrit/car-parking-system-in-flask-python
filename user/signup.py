from flask import render_template,redirect,url_for,request,Blueprint,session
from user.libs import Library
from flask_bcrypt import Bcrypt
import datetime,random,math

bcrypt = Bcrypt()
library = Library()

class Signup:
    signup = Blueprint('signup',__name__,template_folder='templates')
    @signup.route('/user-signup')
    def signup_user():        
        try:
            user = library.check_user()
            if 'id' in session and 'login' in session and user=="user":
                return redirect('/',code=302)
            return render_template('user_signup.html',title="Signup")
        except:
            return render_template('file_not_found.html',title="404")
    
    @signup.route('/user-signup',methods=['POST','GET'])
    def user_verify():
        if request.method =="GET":
            return redirect(url_for('signup_user'))
        elif request.method =="POST":
            name = request.form.get("name")
            gmail = request.form.get("email")
            mobile = request.form.get("phone")
            password = request.form.get("password")
            password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
            confirm_password = request.form.get("confirm_password")
            confirm_password_hash = bcrypt.generate_password_hash(confirm_password).decode('utf-8')
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # return "otp send" 
            mail_otp = ''
            digits = "0123456789"
            first_random =""
            second_random=""
            count = 5
            phone = str(mobile)
            no =""
            for i in range(7):
                first_random+=digits[math.floor(random.random()*10)]
            for i in range(7):
                second_random+=digits[math.floor(random.random()*10)]
            while (count>0):
                no+=phone[-count]
                count=count-1
            user_id = "USER_"+first_random+no+second_random
            insert = library.insert_data(user_id,name,mobile,gmail,password_hash,confirm_password_hash,mail_otp,date)
            if insert =="email exist":
                return "email exist"
            elif insert == "phone exist":
                return "phone exist"
            elif insert == "inserted":
                session['id'] = user_id
                session.permanent = True
                return "otp send"
            elif insert == "not send email":
                return "not send email"
            else:
                return "something went wrong"
                        
        else:
            return render_template('file_not_found.html',title="404")

    @signup.route('/user-signup/email-verification')
    def email_phone_verify():
        try:
            user = library.check_user()
            if 'id' in session and 'login' in session and user=="user":
                return redirect('/',code=302)
            else:
                verify = library.account_verify()
                if session['id'] and verify == "not verify":
                    return render_template('email_phone_verify.html',title= "OTP Verification")
                else:
                    return redirect('/user-signup',code=302)
        except:
            return render_template('file_not_found.html',title="404")

    @signup.route('/user-signup/email-verification',methods=['POST','GET'])
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
                        return redirect('/user-signup',code=302)
                elif request.form.get('email_otp'):
                    email_otp = request.form.get('email_otp')
                    check = library.check_otp(email_otp)
                    if check =="expired":
                        return "otp expired"
                    elif check == "incorrect":
                        return "incorrect otp"
                    elif check == "verify":
                        return "signup successfully"
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







































