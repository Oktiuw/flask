# app/email.py
from flask import render_template

from app import mail, app
from flask_mail import Message

from app.models import User


def send_email(subject: str, sender: str, recipients: list, text_body: str, text_html: str) -> None:
    msg = Message(subject=subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = text_html
    mail.send(msg)


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
