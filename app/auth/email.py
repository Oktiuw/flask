# app/email.py

from flask import render_template, Flask

from app import mail, app

from app.email import send_email
from app.models import User


def send_password_reset_email(user: User) -> None:
    token = user.get_reset_password_token()
    send_email(
        subject='[Mon Application] Réinitialiser le mot de passe',
        sender=app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('email/reset_password.txt', user=user,
                                  token=token),
        text_html=render_template('email/reset_password.html', user=user,
                                  token=token)
    )
