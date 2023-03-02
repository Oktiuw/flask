from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired, EqualTo, Email


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(message='Email requis'), Email(message='Email invalide')])
    submit = SubmitField("Envoyer")


class ResetPasswordForm(FlaskForm):
    password = PasswordField(label='Nouveau mot de passe',
                             validators=[DataRequired(message="Mot de passe requis.")])
    password2 = PasswordField(label='Confirmez le mot de passe',
                              validators=[DataRequired(message="Il faut retaper le mot de passe"),
                                          EqualTo(fieldname='password',
                                                  message="Les deux mots de passe ne sont pas égaux")])
    submit = SubmitField(label='Changer le mot de passe')