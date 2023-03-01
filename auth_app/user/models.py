from itsdangerous import URLSafeTimedSerializer as Serializer
from flask_login import UserMixin
from auth_app import db, app, login_manager
from datetime import datetime, timedelta

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    profile_picture = db.Column(db.String(20), default='default.png')
    messages = db.relationship('Company', backref='user', lazy=True, foreign_keys='Company.user_id')


    def __repr__(self):
        return f"User({self.username}, {self.email})"

    def get_reset_token(self, expiry_period=86400):
        expires_at = int((datetime.utcnow() + timedelta(seconds=expiry_period)).timestamp())
        s = Serializer(app.config['SECRET_KEY'])
        token = s.dumps({'user_id': self.id, 'expires_at': expires_at})
        return token

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        user_id = data.get('user_id')
        expires_at = data.get('expires_at')
        if expires_at < int(datetime.utcnow().timestamp()):
            return None
        return User.query.get(user_id)


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    company_name= db.Column(db.String(30), nullable=False)
    applied=db.Column(db.String(30), nullable=False, default='No')
    Desigination=db.Column(db.String(30), nullable=False)
    Date=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status=db.Column(db.String(30), nullable=False, default='pending')
    remarks=db.Column(db.String(30), nullable=False, default='none')

def __repr__(self):
        return f"Message({self.user_id}, {self.image_name})"












