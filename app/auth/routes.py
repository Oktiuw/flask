from app import db
from app.auth import bp
from app.auth.email import send_password_reset_email
from app.auth.forms import ResetPasswordForm, ResetPasswordRequestForm
from app.main.forms import LoginForm, RegistrationForm
from flask import render_template, flash, redirect, url_for
from app.models import User
from flask_login import current_user, login_user, logout_user
from flask import request
from werkzeug.urls import url_parse


@bp.route('/auth/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Utilisateur ou mot de passe non valide.')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('login.html', title='Enregistrement', form=form)


@bp.route('/auth/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@bp.route('/auth/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Bravo ! Vous devenez un nouvel utilisateur !')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title="S'enregistrer", form=form)





@bp.route('/auth/reset_password_request',methods=["GET", "POST"])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user=user)
        flash(f"Un mail a été envoyé à l'adresse {form.email.data} pour réinitialiser le mot de passe.")
        return redirect(url_for('auth.login'))
    return render_template('reset_password_request.html', form=form)


@bp.route('/auth/reset_password.txt/<token>',methods=["GET", "POST"])
def reset_password(token : str) -> str:
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user = User.verify_reset_password_token(token=token)
    if user:
        form = ResetPasswordForm()
        if form.validate_on_submit():
            user.set_password(form.password.data)
            db.session.commit()
            flash('Votre mot de passe a été modifié.')
            return redirect(url_for('auth.login'))
        return render_template('reset_password.html',title='Redéfinir le mot de passe', form=form)
    return redirect(url_for('main.index'))
