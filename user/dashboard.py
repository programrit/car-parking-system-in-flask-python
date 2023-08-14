from flask import Blueprint as app,render_template,session,redirect,request,url_for,jsonify,current_app
from user.libs import Library
import os,random,string
from datetime import datetime
from werkzeug.utils import secure_filename
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()
library = Library()

class Dashboard: 
    dashboard = app('dashboard',__name__,template_folder="templates")
    @dashboard.route("/")
    def user():
        try:
            user = library.check_user()
            if 'id' in session and 'login' in session and user=="user":
                # check user alredy login redirect to dashboard
                user_data = library.user_data() 
                if user_data == "user not found":
                    session.clear()
                    return redirect('/user-login',code=302)
                else: #else login page
                    notification = library.notification()
                    
                    no_captcha = 6
                    captcha = "".join(random.choices(string.ascii_uppercase+string.digits,k=no_captcha))
                    show_slot = library.show_no_slot()
                    if user_data['profile'] == "" or user_data['profile'] == None: # profile null execute if statement
                        slot = library.show_slot() # slot data show user
                        if slot == "no slot":
                            if notification == "null":
                                return render_template('dashboard.html',title="Dashboard",user_data = user_data,captcha=captcha,show_slot = show_slot)
                            else:
                                return render_template('dashboard.html',title="Dashboard",user_data = user_data,captcha=captcha,show_slot = show_slot,notification=notification)
                        else:
                            if notification == "null":
                                return render_template('dashboard.html',title="Dashboard",user_data = user_data,captcha=captcha,slot=slot,show_slot = show_slot)
                            else:
                                return render_template('dashboard.html',title="Dashboard",user_data = user_data,captcha=captcha,slot=slot,show_slot = show_slot,notification=notification)
                    else: # profile not null execute else statement
                        path = os.path.join('static','user_profile')
                        profile = os.path.join(path,user_data['profile'])
                        slot = library.show_slot()
                        if slot == "no slot":
                            if notification == "null":
                                return render_template('dashboard.html',title="Dashboard",user_data = user_data,profile=profile,captcha=captcha,show_slot = show_slot)
                            else:
                                 return render_template('dashboard.html',title="Dashboard",user_data = user_data,profile=profile,captcha=captcha,show_slot = show_slot, notification=notification)
                        else:
                            if notification == "null":
                                return render_template('dashboard.html',title="Dashboard",user_data = user_data,profile=profile,captcha=captcha,slot=slot,show_slot = show_slot)
                            else:
                                return render_template('dashboard.html',title="Dashboard",user_data = user_data,profile=profile,captcha=captcha,slot=slot,show_slot = show_slot,notification=notification)
            else:
                return redirect('/user-login',code=302)
        except:
            return render_template('file_not_found.html',title="404")
        
    @dashboard.route("/",methods=['POST','GET'])
    def update_user():
        if request.method == 'GET':
            return redirect(url_for("user"))
        elif request.method == 'POST':
            if 'refresh' in request.form: # refresh captcha value
                no_captcha = 6
                captcha = "".join(random.choices(string.ascii_uppercase+string.digits,k=no_captcha))
                return captcha
            # contact data upload database
            elif request.form.get('contact_name') and request.form.get('contact_email') and request.form.get('contact_phone') and request.form.get('contact_message'):
                contact_name = request.form.get('contact_name')
                contact_email = request.form.get('contact_email')
                contact_phone = request.form.get('contact_phone')
                contact_message = request.form.get('contact_message')
                contact = library.contact(contact_name,contact_email,contact_phone,contact_message)
                if contact =="inserted":
                    return "success"
                elif contact == "exist":
                    return "Message already recevied. Team will be contact"
                else:
                    return "Message send failed. Please try again later"
            elif request.form.get('from') and request.form.get('to') and request.form.get('total_days') and request.form.get('amount'):
                from_date = request.form.get('from')
                to_date = request.form.get('to')
                total = request.form.get('total_days')
                amount = request.form.get('amount')
                slot_booking = library.slot_booking(from_date,to_date,total,amount)
                if slot_booking =="booked":
                    return "booking"
                elif slot_booking =="not avilable":
                    return "Slot is not available. Please try again later"
                elif slot_booking == "slot already booked":
                    return "Slot already booked this date. Please book other dates"
                else:
                    return "Slot Booking Faild. Please try again later"
            elif request.form.get("id"):
                id = request.form.get("id")
                delete_slot = library.slot_delete(id)
                if delete_slot == "delete":
                    return "delete"
                elif delete_slot == "slot not found":
                    return "Slot not found"
                else:
                    return "Slot deleted failed"
            elif request.form.get('old_password') and request.form.get('new_password') and request.form.get('confirm_password'):
                old_password = request.form.get('old_password')
                new_password = request.form.get('new_password')
                confirm_password = request.form.get('confirm_password')
                hash_new_password = bcrypt.generate_password_hash(new_password).decode("utf-8")
                hash_confirm_password = bcrypt.generate_password_hash(confirm_password).decode("utf-8")
                update_password = library.password_update(old_password,hash_new_password,hash_confirm_password)
                if update_password == "update":
                    return "update"
                elif update_password == "incorrect password":
                    return "Incorrect old password"
                else:
                    return "Password update failed. Please try again later"

            elif request.form.get("logout"):
                logout = library.logout_all_devices()
                if logout == "logout":
                    session.clear()
                    return "logout"
                else:
                    return "Something went wrong. Please try again later"
            elif request.form.get("value"):
                value = request.form.get("value")
                session['print'] = value
                return "print"
            try:
                profile = request.files.get("profile")
                name = request.form['name']
                if profile == None:
                    profile = "empty"
                    update = library.update_user_data(name,profile)
                    if update == "update":
                        return "update successfully"
                    elif update == "update failed":
                        return "Update Failed. Please try again"
                    else:
                        return "Something went wrong"
                else:
                    file_name = secure_filename(profile.filename)
                    file_ext = os.path.splitext(file_name)[1]
                    file_extension = current_app.config['UPLOAD_EXTENSIONS']
                    if file_ext not in file_extension:
                        return "File extension is not allowed. Only allowed jpg,png,jpeg"
                    else:
                        if int(request.content_length) >100*1024:
                            return "File size is grater than 100kb"
                        elif int(request.content_length) < 5*1024:
                            return "File size is less than 5kb"
                        else:
                            file_name ="IMG-"+datetime.now().isoformat(sep=" ",timespec="seconds").replace(':','').replace('-','').replace(' ','')+str(str(random.randint(99999,999999)))+file_ext
                            profile.save(os.path.join("C:/Users/Ram/Desktop/test/static/user_profile/",file_name))
                            update = library.update_user_data(name,file_name)
                            if update == "update":
                                return "update successfully"
                            elif update == "update failed":
                                return "Update Failed. Please try again"
                            else:
                                return "Something went wrong"
            except Exception as e:
                print(e)
                return e
        else:
            return render_template('file_not_found.html',title="404")
    

    @dashboard.route("/print")
    def print_pdf(): 
        try:
            if 'print' in session and 'id' in session and 'login' in session:
                value = session['print']
                print_pdf = library.print_pdf(value)
                if print_pdf =="failed":
                    return redirect("/",code=302)
                else:
                    return render_template("pdf.html",title = 'Print', print_pdf=print_pdf)
        except:
            return render_template('file_not_found.html',title="404")
        
    



