from admin.AdminClass.admin_login_class import AdminLogin 

class Library:
    def admin_login_verification(self,email,password):
        return AdminLogin.login(self,email,password)