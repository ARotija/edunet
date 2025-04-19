# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models so Alembic sees them when running migrations
    from app import models  

    # Register blueprints (once implemented)
    # from app.auth import auth_bp
    # app.register_blueprint(auth_bp, url_prefix='/auth')
    #
    # from app.attendance import attendance_bp
    # app.register_blueprint(attendance_bp, url_prefix='/attendance')
    #
    # from app.user_views import user_bp
    # app.register_blueprint(user_bp)

    return app
