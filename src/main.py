from dotenv import load_dotenv
load_dotenv()

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_login import LoginManager
from marshmallow.exceptions import ValidationError

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings.app_config")

    db.init_app(app)    
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from commands import db_commands
    app.register_blueprint(db_commands)

    from controllers import registerable_controllers

    for controller in registerable_controllers:
        app.register_blueprint(controller)

    from marshmallow.exceptions import ValidationError

    login_manager.login_view = "users.user_login"
    login_manager.login_message_category = "info"

    @app.errorhandler(ValidationError)
    def handle_bad_request(error):
        return (jsonify(error.messages),400)

    return app