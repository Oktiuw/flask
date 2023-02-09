from flask import render_template, Response
from app import app
from app.forms import LoginForm
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
        return redirect(url_for('/index'))
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
