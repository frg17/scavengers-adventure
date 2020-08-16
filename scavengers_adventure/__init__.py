import os
from flask import Flask, redirect


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'FrOsTiVaRhÉr')
    )

    @app.errorhandler(404)
    def page_not_found(e):
        return redirect('/decrypt')

    from scavengers_adventure.blueprints import index
    app.register_blueprint(index.bp)

    return app
