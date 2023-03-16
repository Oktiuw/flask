# app/forms.py
from io import BytesIO

from flask import current_app, flash
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, validators, FileField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email, Length
from PIL import Image, UnidentifiedImageError

from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Utilisateur', validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    remember_me = BooleanField('Se souvenir de moi')
    submit = SubmitField('Enregistrer')


class RegistrationForm(FlaskForm):
    username = StringField(label='Utilisateur', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Mot de passe', validators=[DataRequired()])
    password2 = PasswordField(label='Répéter le mot de passe',
                              validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Enregistrer")

    # Ajout d’une vérification sur le champ/attribut ‘username’
    def validate_username(self: object, username: StringField) -> None:
        user = User.query.filter(User.username == username.data).first()
        if user is not None:
            raise ValidationError("Choisissez un autre nom.")

    # Ajout d’une vérification sur le champ/attribut ‘email’
    def validate_email(self: object, email: StringField) -> None:
        user = User.query.filter(User.email == email.data).first()
        if user is not None:
            raise ValidationError("Choisissez une autre adresse Email.")


class EditProfileForm(FlaskForm):
    username = StringField(label='Utilisateur', validators=[DataRequired(message="Nom requis.")])
    about_me = StringField(label='A propos de moi', validators=[Length(min=0, max=140, message="Message trop long.")])
    submit = SubmitField("Sauvegarder")

    def __init__(self: object, name: str, *args: tuple, **kargs: dict) -> None:
        FlaskForm.__init__(self, *args, **kargs)
        self.original_username = name

    def validate_username(self: object, username: StringField) -> None:
        if username.data != self.original_username:
            # On recherche si l'utilisateur existe déjà dans la base de données
            if User.query.filter(User.username == username.data).first() is not None:
                raise ValidationError("Ce nom existe déjà, choisissez-en un autre")


class PostForm(FlaskForm):
    def __init__(self: object, *args: tuple, **kargs: dict) -> None:
        FlaskForm.__init__(self, *args, **kargs)
        self._imageData = None

    post = TextAreaField('Message', [validators.length(0, 140, 'Min carac : 0 | Max : 140')])
    image = FileField(id='id_input_file')
    submit = SubmitField("Enregistrer")

    def checkImage(self, image=None):
        if image is not None:
            try:
                im = Image.open(image)
                t = current_app.config['IMG_MAX_SIZE']
                if im.size[0] >= im.size[1]:
                    w = t
                    h = im.size[1] * t // im.size[0]
                else:
                    h = t
                    w = im.size[0] * t // im.size[1]
                im=im.resize((w , h))
                fp = BytesIO()
                im.save(fp, format='JPEG')
                self._imageData = fp.getvalue()
            except FileNotFoundError:
                raise ValidationError('Fichier non trouvé')
            except UnidentifiedImageError:
                raise ValidationError('Format non reconnu')
            except OSError:
                raise ValidationError('Conversion JPEG impossible')
    def getImageData(self):
        return self._imageData

    def validate(self, extra_validators=None):

        if not super(PostForm, self).validate():
            return False
        if not self.post.data and not self.image.data:
            flash("On ne peut pas enregistrer un message vide")
            return False
        return True