from flask import render_template
from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect


@app.route('/')
@app.route('/index')
def index() -> str:
    user = {'username': 'Aurélien et Harun '}
    posts = [
        {
            'author': {'username': 'John'},
            'body': "Flask, c'est super !"
        },
        {
            'author': {'username': 'Suzan'},
            'body': "C'est encore mieux que Symfony ! Oups !"
        }
    ]
    return render_template('index.html', user=user, posts=posts)


@app.route('/apropos')
def apropos() -> str:
    return render_template('apropos.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Enregistrement demandé pour l’utilisateur {form.username.data}, Se souvenir = {form.remember_me.data}")
        return redirect('/index')
    return render_template('login.html', title='Enregistrement', form=form)
