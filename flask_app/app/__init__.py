from flask import Flask

from app.config import Config
from app.extensions import db, bcrypt, jwt
from app.auth import auth_bp


def create_app():
    """
    Application Factory
    """

    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp)

    return app