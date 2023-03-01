from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ujieveiThae1fa3fuchiec2keighahe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_USE_TLS'] = 587 
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '' 
app.config['MAIL_PASSWORD'] = '' 
app.config['UPLOAD_FOLDER'] = 'auth_app/static/uploads'
app.app_context().push()
 


login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = 'You must be logged in'
login_manager.login_message_category = 'info'

db = SQLAlchemy(app)
mail = Mail(app)
bcrypt = Bcrypt(app)


def run():
    from auth_app.auth import auth
    from auth_app.user import user

    import auth_app.auth.routes
    import auth_app.user.routes

    app.register_blueprint(auth)
    app.register_blueprint(user)
    
    
