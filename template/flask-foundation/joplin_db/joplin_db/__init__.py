#! ../env/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Nathan Genetzky'
__email__ = 'nathan@genetzky.us'
__version__ = '0.1.0.dev0'

from flask import Flask
from webassets.loaders import PythonLoader as PythonAssetsLoader

from joplin_db.controllers.main import main
from joplin_db import assets
from joplin_db.models import db

from joplin_db.extensions import (
    cache,
    assets_env,
    debug_toolbar,
    login_manager
)


def create_app(object_name):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name: the python path of the config object,
                     e.g. joplin_db.settings.ProdConfig

        env: The name of the current environment, e.g. prod or dev
    """

    app = Flask(__name__)

    app.config.from_object(object_name)

    # initialize the cache
    cache.init_app(app)

    # initialize the debug tool bar
    debug_toolbar.init_app(app)

    # initialize SQLAlchemy
    db.init_app(app)

    login_manager.init_app(app)

    # Import and register the different asset bundles
    assets_env.init_app(app)
    assets_loader = PythonAssetsLoader(assets)
    for name, bundle in assets_loader.load_bundles().items():
        assets_env.register(name, bundle)

    # register our blueprints
    app.register_blueprint(main)

    return app
