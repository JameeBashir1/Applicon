from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
            DataRequired(),
            Length(min=2, max=30)
        ])

    email = StringField('Email', validators=[
            DataRequired(),
            Email(),
            Length(min=2, max=120)
        ])

    password = PasswordField('Password', validators=[
            DataRequired(),
            Length(min=8, max=120)
        ])

    confirm_password = PasswordField('Confirm Password', validators=[
            DataRequired(),
            EqualTo('password'),
            Length(min=8, max=120)
        ])
    

    submit = SubmitField('Request Access')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
            DataRequired(),
            Email(),
            Length(min=2, max=120)
        ])

    password = PasswordField('Password', validators=[
            DataRequired(),
            Length(min=8, max=120)
        ])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')


class ResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[
            DataRequired(),
            Email(),
            Length(min=2, max=120)
        ])

    submit = SubmitField('Request Password Reset ')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[
            DataRequired(),
            Length(min=8, max=120)
        ])

    confirm_password = PasswordField('Confirm Password', validators=[
            DataRequired(),
            EqualTo('password'),
            Length(min=8, max=120)
        ])

    submit = SubmitField('Reset Password')
