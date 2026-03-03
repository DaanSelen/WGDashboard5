#!/bin/env python3

import logging as log

import flask
import json
import os

from modules.config.reader import reader
from modules.database.database import database
from modules.utilities.utilities import utilities as util

from modules.routes.routes import routes

if __name__ == '__main__':
    log.basicConfig(level=log.DEBUG)

    ok, config_contents = reader.read_config()
    if not ok:
        exit(1)

    found, config_database = util.filter_config(config_contents, 'DATABASE')
    if not found:
        exit(1)

    ok, engine, session = database.create_session(config_database)
    ok = database.ensure_contents(engine)

    app = flask.Flask("WGDashboard", template_folder=os.path.abspath("./static/dist/WGDashboardAdmin"))
    app.register_blueprint(routes)

    app.wgdashboard_config = config_contents
    app.engine = engine
    app.db_session = session

    app.run(debug=True, use_reloader=False)