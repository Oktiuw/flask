from datetime import datetime

from flask import render_template, Response
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm
from flask import render_template, flash, redirect, url_for
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required
from flask import request
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
@login_required
def index() -> str:
    # user = {'username': 'Aurélien et Harun '}
    # posts = [
    # {
    #   'author': {'username': 'John'},
    #   'body': "Flask, c'est super !"
    # },
    # {
    #   'author': {'username': 'Suzan'},
    #  'body': "C'est encore mieux que Symfony ! Oups !"
    # }
    # ]
    return render_template('index.html', title='Accueil')


@app.route('/apropos')
def apropos() -> str:
    return render_template('apropos.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Utilisateur ou mot de passe non valide.')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Enregistrement', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Bravo ! Vous devenez un nouvel utilisateur !')
        return redirect(url_for('login'))
    return render_template('register.html', title="S'enregistrer", form=form)


@app.route('/user/<username>')
@login_required
def user(username: str) -> str:
    user = User.query.filter(User.username == username).first_or_404('Accès refusé')
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Vos modification ont été enregistrées.')
        return redirect(url_for('user',username=current_user.username))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
