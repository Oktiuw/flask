# app/gestionnaire.py
from flask import render_template
from werkzeug.exceptions import HTTPException, NotFound, InternalServerError, RequestEntityTooLarge

from app import db
from app.erreurs import bp


@bp.app_errorhandler(NotFound)
def not_found_error(error: HTTPException):
    return render_template('404.html'), 404


@bp.app_errorhandler(InternalServerError)
def internal_error(error: HTTPException):
    db.session.rollback()
    return render_template('500.html'), 500
@bp.app_errorhandler(RequestEntityTooLarge)
def not_found_error(error: HTTPException):
    return render_template('413.html'), 404