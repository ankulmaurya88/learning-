import os

from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


class Config:
    """Base application configuration."""

    # Flask
    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret-key")

    # Database
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT
    JWT_SECRET_KEY = os.getenv(
        "JWT_SECRET_KEY",
        "change-this-jwt-secret"
    )

    # Optional JWT configuration
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 hour