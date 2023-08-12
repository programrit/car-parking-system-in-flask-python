from user.UserClass.new_user import NewUser
from user.UserClass.check_user import UserFound
from user.UserClass.user_login import UserLogin
from user.UserClass.contact import Contact
from user.UserClass.slot import Slot
from user.UserClass.password_update import PasswordUpdate



class Library:
    # insert into databse
    def insert_data(self,user_id,name,mobile,gmail,password,confirm_password,mail_otp,date):
        return NewUser.insert(self,user_id,name,mobile,gmail,password,confirm_password,mail_otp,date)
    # check user exist or not
    def check_user(self):
        return UserFound.check_user_exist(self)
        
    # check email already verified or not
    def account_verify(self):
        return UserFound.email_verify(self)

    # enter otp is correct or wrong (otp verification)
    def check_otp(self,email_otp):
        return UserFound.otp_verification(self,email_otp)

    # resend otp and update database
    def otp_update(self):
        return UserFound.resend_otp(self)
    
    # login user
    def login(self,gmail,password):
        return UserLogin.user_login(self,gmail,password)

    # user data share     
    def user_data(self):
        return UserLogin.share_user_data(self)

    # update user data
    def update_user_data(self,name,email,phone,profile):
        return UserLogin.update_user(self,name,email,phone,profile)

    #contact team send message 
    def contact(self,contact_name,contact_email,contact_phone,contact_message):
        return Contact.contact_team(self,contact_name,contact_email,contact_phone,contact_message)

    # slot booking   
    def slot_booking(self,from_date,to_date,total,amount):
       return Slot.new_slot_booking(self,from_date,to_date,total,amount)

    # cancel slot
    def slot_delete(self,id):
       return Slot.slot_cancel(self,id)

    # show slot data
    def show_slot(self):
       return Slot.show_slot_data(self)

    # show no of slot available
    def show_no_slot(self):
        return Slot.no_of_slot_available(self)

    # password databse login user
    def password_update(self,old_password,new_password,confirm_password):
        return PasswordUpdate.update_password(self,old_password,new_password,confirm_password)

    # forget password
    def forget_password(self,gmail):
        return PasswordUpdate.forget_password_in_user(self,gmail)

    # otp verfication for forget password
    def check_otp_forget(self,email_otp):
        return PasswordUpdate.otp_send_for_forget_password(self,email_otp)
    
    # check validate time in forget password
    def check_new_password(self):
       return PasswordUpdate.update_new_password_time_validation(self)


    # password update database forget user
    def update_password(self,new_password,confirm_password):
        return PasswordUpdate.password_update_database(self,new_password,confirm_password)

    # printout slot
    def print_pdf(self,id):
        return Slot.print_slot(self,id)

    # logout    
    def logout_all_devices(self):
       return UserLogin.logout(self)

    # show notification
    def notification(self):
        return NewUser.notification_show(self)
        


        

    


