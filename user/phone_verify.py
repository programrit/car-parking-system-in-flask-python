import math,random
from twilio.rest import Client
from flask import current_app

class Phone:
    digits="0123456789"
    OTP =""
    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
    def __init__(self,phone):
        self.phone = phone
    def send_otp_phone(self):
        phone_no = self.phone
        otp = self.OTP
        try:
            account_sid = '{}'.format(current_app.config['API_KEY'])
            auth_token = '{}'.format(current_app.config['API_SECRET'])
            client = Client(account_sid, auth_token)
            message = client.messages.create(
            from_='+13203818477',
            body='Your OTP is {}'.format(otp),
            to='+91{}'.format(phone_no)
            )   
            return "{},{}".format(message.status,otp)
        except Exception  as e:
            return "not send"