from flask import Flask 
from flask_mail import Mail 
 
app = Flask(__name__) 
app.config['SECRET_KEY'] = 'random' 
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io' 
app.config['MAIL_PORT'] = '2525' # (or try 2525) 
app.config['MAIL_USERNAME'] = '705a8fec11bf45' 
app.config['MAIL_PASSWORD'] = 'ea89051ad656fb' 
 
mail = Mail(app) 
from app import views 