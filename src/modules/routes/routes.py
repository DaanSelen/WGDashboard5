#!/bin/env python3

import flask

from .response import make_resp_obj
from ..database.functions import functions
from ..utilities.utilities import utilities

routes = flask.Blueprint("routes", __name__)

@routes.before_request
def auth_required():
    if flask.request.method.lower() == "options":
        return make_resp_obj(True, "", flask.jsonify({"status": True}), 200)

    ok, config_server = utilities.filter_config(flask.current_app.wgdashboard_config, 'SERVER')
    if not ok:
        return make_resp_obj(False, "Internal Error", {}, 500)

    auth_required = config_server.get('auth_req', True) # Set to true for a safe default

    if not auth_required:
        return
    
    whiteList = [
        '/client',
        '/static/',
        '/fileDownload',
        'validateAuthentication',
        'authenticate',
        'getDashboardConfiguration',
        'getDashboardTheme',
        'getDashboardVersion',
        'sharePeer/get',
        'isTotpEnabled',
        'locale'
    ]

    request_path = flask.request.path
    http_headers = flask.request.headers
    api_key = http_headers.get("wgdashboard-apikey")

    api_key_enabled = config_server.get("wgdashboard_apikey", False)
    registered_api_keys = functions.retrieve_api_keys(flask.current_app.db_session)

    if not api_key:
        response = make_resp_obj()
        return response

@routes.route("/")
def index():
    return make_resp_obj(True, "/ Endpoint", flask.jsonify({"message": "Hello from routes file!"}), 200)

@routes.route("/health")
@routes.route("/healthz")
def health():
    return make_resp_obj(True, "Health Endpoint", flask.jsonify({"status": "ok"}), 200)