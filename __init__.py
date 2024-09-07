from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Configurer l'application ici (par exemple, charger les variables d'environnement)

    # Enregistrer les blueprints
    from .main_flask import main_flask_main
    from .discord_main import main_discord_main
    
    app.register_blueprint(main_flask_main)
    app.register_blueprint(main_discord_main)
    
    return app

create_app()