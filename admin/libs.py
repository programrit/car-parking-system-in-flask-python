from admin.AdminClass.admin_login_class import AdminLoginVerify 
from admin.AdminClass.admin_dashboard_class import AdminDashboardVerify

class Library:

    #login admin
    def admin_login_verification(self,email,password):
        return AdminLoginVerify.login(self,email,password)

    # admin verification

    def admin_exist(self):
        return AdminDashboardVerify.admin_is_found_or_not(self)