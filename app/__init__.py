# app/__init__.py
from flask import Flask
from flask_moment import Moment

from app.config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_login import LoginManager

# Création de l'application
# __name__ contient le nom de l'application : app
app = Flask(__name__)
app.config.from_object(Config)
# Démarrage du moteur de la base de données
db = SQLAlchemy(app)
# Démarrage de l'outil de migration associé à la base de données
migrate = Migrate(app, db)

# Instanciation du module de gestion des connexions
login = LoginManager(app)
# Fonction de vue de redirection
login.login_view = 'login'
login.login_message = 'Il faut être connecté pour accèder à cette page'

moment = Moment(app)
# On importe le fichier contenant
# la définition des fonctions de vue
# ainsi que celui des modèles
from app import routes, models
