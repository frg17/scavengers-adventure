import os
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_mapping(
        SECRET_KEY = os.environ.get('SECRET_KEY', 'FrOsTiVaRhÉr')
    )


    @app.route('/')
    def index():
        return (
            "<!DOCTYPE html>"
            "<html> <head> <title>Scavenger's Adventure</title></head>"
            "<body><h2>Welcome to the Scavenger's adventure!</h2></body></html>"
        )


    return app

