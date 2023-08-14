from admin.AdminClass.admin_login_class import AdminLoginVerify 
from admin.AdminClass.admin_dashboard_class import AdminDashboardVerify
from admin.AdminClass.user_table_class import UserTableData
from admin.AdminClass.slot_booking_table_class import SlotBookingTable
from admin.AdminClass.user_other_device_table_class import UserOtherTableData
from admin.AdminClass.admin_table_class import AdminTableData
from admin.AdminClass.admin_other_device_table_class import AdminOtherTableData
from admin.AdminClass.settings_class import SettingChangePassword


class Library:

    #login admin
    def admin_login_verification(self,email,password):
        return AdminLoginVerify.login(self,email,password)

    # admin verification
    def admin_exist(self):
        return AdminDashboardVerify.admin_is_found_or_not(self)
    
    # total no of user
    def no_user(self):
        users = AdminDashboardVerify.no_users(self)
        if users != "no user":
            return users
        else:
            return "Null"

    # total no of other device user
    def other_device_user(self):
        other_user = AdminDashboardVerify.other_device_users(self)
        if other_user !="no user":
            return other_user
        else:
            return "Null" 
    
    # total no of admin
    def admin(self):
        admin_data = AdminDashboardVerify.no_admins(self)
        if admin_data != "no admin":
            return admin_data
        else:
            return "Null"
    
    # total no slot available
    def no_slot(self):
        slot = AdminDashboardVerify.slot_available(self)
        if slot != "no slot":
            return slot
        else:
            return "Null"

    # user data fetch in database show user table  
    def user_data(self):
        return UserTableData.users_data(self)
        
    # slot data fetch in database show slot booking table  
    def slot_data(self):
        return SlotBookingTable.user_slot_booking(self)
    
    # other devie user data fetch in database show user table  
    def other_device_user_data(self):
        return UserOtherTableData.user_other_table_data(self)
    
    # admin data fetch in database show user table  
    def admin_data(self):
        return AdminTableData.admins_data(self)
    
    # other devie admin data fetch in database show user table  
    def other_device_admin_data(self):
        return AdminOtherTableData.admin_other_table_data(self)
    
    # add new user from admin
    def add_new_user(self,user_id,name,mobile,gmail,password_hash,confirm_password_hash):
        return UserTableData.add_new_user_in_admin(self,user_id,name,mobile,gmail,password_hash,confirm_password_hash)

    # add new admin from admin
    def add_new_admin(self,user_id,name,gmail,password):
        return AdminTableData.add_new_admin_in_admin(self,user_id,name,gmail,password)
    
    # fetch particular data show modal in update
    def show_update_data(self,user_id):
        return UserTableData.send_data_update(self,user_id)

    # update user data
    def update_user_data(self,user_id,name):
        return UserTableData.update_user_data_in_admin(self,user_id,name)
    
    # delete user data
    def delete_user_data(self,delete_id):
        return UserTableData.delete_user_data_in_admin(self,delete_id)
    
    # delete admin data
    def delete_admin_data(self,admin_id):
        return AdminTableData.delete_admin_data_in_admin(self,admin_id)

    # delete other device login user
    def delete_other_user_data(self,other_user_id):
        return UserOtherTableData.delete_other_user_data_in_admin(self,other_user_id)

    # delete user slot data
    def delete_user_slot_data(self,slot_id):
        return SlotBookingTable.delete_user_slot_in_admin(self,slot_id)
    
    # delete other device login admin
    def delete_other_admin_data(self,other_admin_id):
        return AdminOtherTableData.delete_other_admin_data_in_admin(self,other_admin_id)

    # fetch current admin data

    def current_admin_data(self):
        current_admin = AdminTableData.current_admin_data(self)
        if current_admin !="no admin":
            return current_admin
        else:
            return "Null"
        
    # change password
    def change_password(self,old_password,new_password):
        delete = SettingChangePassword.delete_other_account_password(self)
        if delete == "delete":
            return SettingChangePassword.change_password_settings(self,old_password,new_password)
        else:
            return SettingChangePassword.change_password_settings(self,old_password,new_password)
        
    # logout
    def logout_user(self):
        return AdminDashboardVerify.delete_other_account_in_logout(self)



    


