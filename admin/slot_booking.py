from flask import Blueprint,render_template,redirect,session,request

from admin.libs import Library



library = Library()
class UserSlotBooking:
    slot_booking = Blueprint('slot_booking',__name__,template_folder='templates')
    @slot_booking.route('/user-slot-table')
    def user_slot_data():
        try:
            admin = library.admin_exist()
            if 'admin_id' in session and 'login' in session and admin == "admin":
                slot_data = library.slot_data()
                current_admin_data = library.current_admin_data()
                if slot_data != "no slot":
                    return render_template('__slot_booking_table.html',title="Slot Booking Data",slot_data=slot_data,current_admin_data=current_admin_data)
                else:
                    return render_template('__slot_booking_table.html',title="Slot Booking Data",current_admin_data=current_admin_data)
            else:
                session.clear()
                return redirect('/admin-login', code=302)
        except:
            return render_template('404.html',title="404")
        
    
    @slot_booking.route('/user-slot-table',methods=['POST','GET'])
    def delete_slot_booking():
        if request.method == 'GET':
            return redirect('/user-slot-table',code=302)
        elif request.method =='POST':
            if request.form.get('slot_id'):
                slot_id = request.form.get('slot_id')
                delete = library.delete_user_slot_data(slot_id)
                if delete == "delete":
                    return "delete"
                elif delete == "failed":
                    return "User data delete failed. Please try again later"
                else:
                    return "Something went wrong"
            else:
                return render_template('404.html',title="404")
        else:
            return render_template('404.html',title="404")
     