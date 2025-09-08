from flask import Flask 

from .routes import main

# a func for creating the app, is better than just inititalizing the app! 
def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    app.register_blueprint(main)

    return app