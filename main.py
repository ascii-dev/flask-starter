"""Module for application factory"""

from flask import Flask
from flask_migrate import Migrate
from flask_restplus import Api

from config import AppConfig

from api import api_blueprint
from api.models.database import db

api = Api(api_blueprint, doc='/')


def create_app(config=AppConfig):
    """Return app object given config object"""

    app = Flask(__name__)
    app.config.from_object(config)
    app.url_map.strict_slashes = False
    app.register_blueprint(api_blueprint)

    # bind app to db
    db.init_app(app)

    import api.models
    # import pdb; pdb.set_trace()
    import api.views

    # initialize migration scripts
    migrate = Migrate(app, db)

    return app
