from flask import render_template
from app import app


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
def apropos()->str:
    return render_template('apropos.html')