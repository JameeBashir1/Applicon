from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField,RadioField
from wtforms.validators import DataRequired,  EqualTo, Length





class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old Password', validators=[
            DataRequired(),
            Length(min=8, max=120)
        ])

    new_password = PasswordField('New Password', validators=[
            DataRequired(),
            Length(min=8, max=120)
        ])

    new_confirm_password = PasswordField('Confirm New Password', validators=[
            DataRequired(),
            EqualTo('new_password'),
            Length(min=8, max=120)
        ])

    submit = SubmitField('Change Password')


class UpdateProfilePictureForm(FlaskForm):
    picture = FileField('', validators=[
            FileAllowed(['png', 'jpg', 'jpeg'])
        ])

    submit = SubmitField('Update')

class UploadForm(FlaskForm):
    company=StringField('Company Name *',validators=[DataRequired()])
    apply=RadioField ('Applied *',choices=[('Yes','Yes'),('No','No')],validators=[DataRequired()])
    designation=StringField('Applied For *',validators=[DataRequired()])
    status=StringField('Status *',validators=[DataRequired()])
    remarks=StringField('Remarks *',validators=[DataRequired()])
    submit = SubmitField('Upload')

class UpdateForm(FlaskForm):
    company=StringField('Company Name *',validators=[DataRequired()])
    apply=RadioField ('Applied *',choices=[('Yes','Yes'),('No','No')],validators=[DataRequired()])
    designation=StringField('Applied For *',validators=[DataRequired()])
    status=StringField('Status *',validators=[DataRequired()])
    remarks=StringField('Remarks *',validators=[DataRequired()])
    submit = SubmitField('Update')











