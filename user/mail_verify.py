# from flask_mail import Mail,Message,current_app
import math,random
import smtplib
from flask import current_app


class email:
    digits="0123456789"
    OTP =""
    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
    def __init__(self,email):
        self.email = email
    def send_otp_email(self):
        From = "photograms19@gmail.com"
        to = self.email
        otp = self.OTP
        subject ="Email Verification"
        body="Your OTP is {} \n\n Don't Share with anyone. OTP is valid for 15 min only!".format(otp)
        # print(current_app.logger.debug(msg.send(msg)))
        # msg = Message("",sender=sender,recipients=[gmail])
        message ='Subject: {}\n\n{}'.format(subject,body)
        try:
            gmail = smtplib.SMTP(current_app.config['MAIL_SERVER'],current_app.config['MAIL_PORT'])
            gmail.starttls()
            gmail.login(f"{current_app.config['MAIL_USERNAME']}",f"{current_app.config['MAIL_PASSWORD']}")
            gmail.sendmail(From,to,message)
            gmail.quit()
            return "{},{}".format("otp send",otp)
        except Exception as e:
            print(e)
            return "not send"
        
    def send_email_user(self,device):
        From = "photograms19@gmail.com"
        to = self.email
        info = device
        subject ="Email Verification"
        body="Someone is trying login user account \n\n Device info: {}. \n\n If you logout from your current device automatically logout from all the devices".format(info)
        # print(current_app.logger.debug(msg.send(msg)))
        # msg = Message("",sender=sender,recipients=[gmail])
        message ='Subject: {}\n\n{}'.format(subject,body)
        try:
            gmail = smtplib.SMTP(current_app.config['MAIL_SERVER'],current_app.config['MAIL_PORT'])
            gmail.starttls()
            gmail.login(f"{current_app.config['MAIL_USERNAME']}",f"{current_app.config['MAIL_PASSWORD']}")
            gmail.sendmail(From,to,message)
            gmail.quit()
            return "send"
        except Exception as e:
            print(e)
            return "not send"
            
        

