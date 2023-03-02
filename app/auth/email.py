# app/email.py
from threading import Thread

from flask import render_template, Flask

from app import mail, app
from flask_mail import Message

from app.models import User


def send_email(subject: str, sender: str, recipients: list, text_body: str,text_html: str) -> None:
    msg = Message(subject=subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = text_html
    Thread(target=send_async_email, args=(app, msg)).start()


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


def send_async_email(app: Flask, msg: Message) -> None:
    with app.app_context():
        mail.send(msg)
