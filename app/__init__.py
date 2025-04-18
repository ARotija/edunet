from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models to create tables
    from app import models  

    # Register blueprints (later)
    # from app.auth import bp as auth_bp
    # app.register_blueprint(auth_bp)
    # ...

    return app
