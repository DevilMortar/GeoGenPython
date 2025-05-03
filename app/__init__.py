from flask import Flask
from app.routes import geogen_bp

def create_app():
    app = Flask(__name__)

    # Enregistrer les blueprints
    app.register_blueprint(geogen_bp)

    # Ajouter d'autres configurations ou extensions ici

    return app