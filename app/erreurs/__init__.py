from flask import Blueprint

bp = Blueprint('erreurs', __name__, template_folder='templates')
from app.erreurs import gestionnaire
