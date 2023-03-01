from flask import url_for, flash
from flask_mail import Message
from auth_app.user.models import User
from auth_app import mail
import smtplib
import os




def send_reset_email(user):
    token = user.get_reset_token()
    message = f'''To reset your password visit the following link:
        {url_for('auth.reset_password', token=token, _external=True)}
        '''
    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login('<haqasrar816@gmail.com>','<Aasrarhh@123>')
    mail.sendmail('<haqasrar816@gmail.com>',user.email,message)
    mail.close()
    flash("An email is sent to your email account", "success")