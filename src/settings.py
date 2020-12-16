import os

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "Dev Key"

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.getenv("DB_URI")
        if not value:
            raise ValueError("DB_URI is not set!")
        return value

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    @property
    def JWT_SECRET_KEY(self):
        value = os.environ.get("JWT_SECRET_KEY")                    # Use the production JWT secret
        if not value:
            raise ValueError("JWT Secret Key is not set")           # If no JWT then raise "JWT Secret Key is not set" error

        return value                                                # Return the JWT

class TestingConfig(Config):
    TESTING = True

#Which configuration we should look up
environment = os.getenv("FLASK_ENV")

if environment == "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()