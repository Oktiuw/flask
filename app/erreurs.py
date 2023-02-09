# app/erreurs.py
from flask import render_template
from werkzeug.exceptions import HTTPException, NotFound, InternalServerError
from app import app, db
@app.errorhandler(NotFound)
def not_found_error(error : HTTPException):
    return render_template('404.html'), 404

@app.errorhandler(InternalServerError)
def internal_error(error: HTTPException):
    db.session.rollback()
    return render_template('500.html'), 500