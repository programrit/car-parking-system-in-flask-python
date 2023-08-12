from dotenv import load_dotenv
import os,datetime


load_dotenv()
class Config(object):
    SECRET_KEY = '{}'.format(os.getenv("key"))
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=100)
    UPLOAD_EXTENSIONS = ['.jpg','.png','.jpeg']
    # MAX_CONTENT_LENGTH =100*1024
    UPLOAD_PATH = 'static/user_profile/'

class EmailConfig(Config):
    DEBUG = True
    MAIL_SERVER = "{}".format(os.getenv("email"))
    MAIL_PORT = os.getenv("port")
    MAIL_USERNAME  = "{}".format(os.getenv("send_mail"))
    MAIL_PASSWORD = "{}".format(os.getenv("password"))
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_DEBUG = True
    MAIL_SUPPRESS_SEND = False
    API_KEY="{}".format(os.getenv("sid"))
    API_SECRET="{}".format(os.getenv("token"))
    
class DatabaseConfig(Config):
    DEBUG = True
    MYSQL_HOST = '{}'.format(os.getenv("host"))
    MYSQL_USER = '{}'.format(os.getenv("user"))
    MYSQL_PASSWORD = '{}'.format(os.getenv("db_password"))
    MYSQL_DB = '{}'.format(os.getenv("db"))
    

       

        