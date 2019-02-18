from flask import Flask
from flask_mail import Mail
app = Flask(__name__)
app.config['SECRET_KEY'] = 'info-3180'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = '5cdc8153265a3d'
app.config['MAIL_PASSWORD'] = 'c4c64c1b0df960'
mail = Mail(app)
from app import views