import logging
from flask import Flask
from pprint import pformat
from flask.ext.sqlalchemy import SQLAlchemy

import wikiarguments_config

logg = logging.getLogger(__name__)

app = None
db = None

def make_app(**app_options):
    global db, app
    app = Flask(__name__)
    logging.basicConfig(level=logging.INFO)
    logg.info("creating flask app %s", __name__)
    app.config.from_object(wikiarguments_config)
    if app_options:
        app.config.update(app_options)
    logg.info("using database URI: '%s'", app.config["SQLALCHEMY_DATABASE_URI"])
    logg.debug("config is %s", pformat(dict(app.config)))

    app.config["RESTFUL_JSON"] = {'ensure_ascii': False}
    db = SQLAlchemy(app)

    import wikiarguments_rest.views
    import wikiarguments_rest.api
    return app

