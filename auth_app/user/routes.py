                                                                                                                                                                                                                                                                                                   
from flask import render_template, url_for, flash, redirect,request
from flask_login import login_required, current_user,logout_user
from werkzeug.utils import secure_filename
from auth_app import app
import os
from auth_app import db, bcrypt
from auth_app.user import user
from auth_app.user.forms import  ChangePasswordForm, UpdateProfilePictureForm,UploadForm,UpdateForm
from auth_app.user.utils import save_picture
from auth_app.user.models import User,Company


@app.errorhandler(Exception)
def handle_exception(e):
    # log the exception
    app.logger.error(e)

    # show a generic error page
    return render_template('error.html'), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html')



@user.route('/addcompany', methods=['GET', 'POST'])
@login_required
def addcompany():
    form = UploadForm()
    if request.method == 'POST' and form.validate():
        company=Company.query.filter_by(user_id=current_user.id).first()
        company_name=form.company.data
        applied=form.apply.data
        Desigination=form.designation.data
        status=form.status.data
        remarks=form.remarks.data
        new_company=Company(company_name=company_name,applied=applied,Desigination=Desigination,status=status,remarks=remarks,user_id=current_user.id)
        if Company.query.filter_by(company_name=company_name).first():
            companies = [company]
            return render_template('Allcompanies.html', title='addcompany',companies=companies)
        else:
            db.session.add(new_company)
            db.session.commit()
            flash('Company added successfully', 'success')

            companies = Company.query.filter_by(user_id=current_user.id).all()
            return render_template('Allcompanies.html', title='addcompany',companies=companies)
    return render_template('addcompany.html', title='addcompany',form=form)


@user.route('/Allcompanies', methods=['GET', 'POST'])
@login_required
def Allcompanies():
    companies=Company.query.all()
    return render_template('Allcompanies.html', title='Allcompanies',companies=companies)


@user.route('/delete_history', methods=['GET', 'POST'])
@login_required
def delete_history():
    if request.method == 'POST':
        ids = request.form.getlist('checkbox')
        if not ids:
            flash('No files selected', 'warning')
            return redirect(url_for('user.Allcompanies'))
        for id in ids:
            company = Company.query.filter_by(id=int(id)).first()
            db.session.delete(company)
        db.session.commit()
        flash('Files have been deleted', 'success')
    return redirect(url_for('user.Allcompanies'))

@user.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    company = Company.query.get_or_404(id)
    form = UpdateForm(obj=company) # populate form fields with company data

    if request.method == 'POST' and form.validate():
        company.company_name = form.company.data
        company.applied = form.apply.data
        company.Desigination = form.designation.data
        company.status = form.status.data
        company.remarks = form.remarks.data
        db.session.commit()
        flash('Company updated successfully', 'success')
        return redirect(url_for('user.Allcompanies'))

    return render_template('update.html', title='update', form=form, company=company)





@user.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    change_password_form = ChangePasswordForm()
    update_profile_picture_form = UpdateProfilePictureForm()

    if change_password_form.validate_on_submit():
        if bcrypt.check_password_hash(current_user.password, change_password_form.old_password.data):
            new_hashed_password = bcrypt.generate_password_hash(change_password_form.new_password.data)
            current_user.password = new_hashed_password
            db.session.commit()
            flash("Password changed successfully", "success")
            return redirect(url_for('auth.logout'))
        else:
            flash("Invalid Password", "danger")
    elif update_profile_picture_form.validate_on_submit():
        profile_picture = save_picture(update_profile_picture_form.picture.data)
        current_user.profile_picture = profile_picture
        db.session.commit()
        flash("Profile Picture Updated!", "success")

    profile_picture = url_for('static', filename='profile_pictures/' + current_user.profile_picture)

    return render_template(
            'account.html',
            title='account',
            profile_picture=profile_picture,
            change_password_form=change_password_form,
            update_profile_picture_form=update_profile_picture_form
        )