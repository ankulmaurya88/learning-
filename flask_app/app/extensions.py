from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

# Database
db = SQLAlchemy()

# Password hashing
bcrypt = Bcrypt()

# JWT Authentication
jwt = JWTManager()