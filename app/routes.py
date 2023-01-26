from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index() -> str:
 user = { 'username' : 'Aurélien et Harun les majors' }
 return render_template('index.html', title='Page principale', user=user)