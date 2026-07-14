def create_app():
    
    app = Flask(__name__)

    app.config.from_object(Config)

    # init_db(app)
    # init_jwt(app)
    # init_bcrypt(app)

     # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp)

    return app