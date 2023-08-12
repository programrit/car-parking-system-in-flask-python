from flask import Blueprint,render_template,redirect,session

from admin.libs import Library



library = Library()
class UserSlotBooking:
    slot_booking = Blueprint('slot_booking',__name__,template_folder='templates')
    @slot_booking.route('/user-slot-table')
    def user_slot_data():
        try:
            admin = library.admin_exist()
            if 'admin_id' in session and 'login' in session and admin == "admin":
                return render_template('__slot_booking_table.html',title="Slot Booking Data")
            else:
                session.clear()
                return redirect('/admin-login', code=302)
        except:
            return render_template('404.html',title="404")
     