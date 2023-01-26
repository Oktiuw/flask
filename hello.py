# hello.py
from flask import Flask

# Création de l’application :
app = Flask(__name__)


# Définition d’une fonction de "vue" accrochée
# au lien / (route)
@app.route("/")
def hello() -> str:
    return  """
<!doctype html>
    <html lang="fr">
        <head>
             <meta charset="utf-8">
             <meta name="description" content="Ma première page Flask.">
             <meta name="keywords" content="Flask">
             <meta name="author" content="moi-même">
             <title>Ma première page Flask</title>
        </head>
        <body>
             <h1>Ma première page Flask</h1>
             <p>Flask est vraiment super !</p>
             <hr/>
        </body>
    </html>
"""


# Lancement de l’application
# On vérifie que l’application n’est pas lancée depuis un serveur Jupiter ou autre
if __name__ == "__main__":
    app.run()
