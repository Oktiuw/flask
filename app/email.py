from flask_mail import Message
from threading import Thread

from flask import Flask, current_app

from app import mail


def send_email(subject: str, sender: str, recipients: list, text_body: str, text_html: str) -> None:
    msg = Message(subject=subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = text_html
    Thread(target=send_async_email, args=(current_app._get_current_object(), msg)).start()


def send_async_email(app: Flask, msg: Message) -> None:
    with app.app_context():
        mail.send(msg)
