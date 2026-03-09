#!/bin/env python3

import flask
import json

def make_resp_obj(status=True, message=None, data=None, http_code=200):
    if data is None:
        data = {}

    resp_json_data = json.dumps({
        "status": status,
        "message": message,
        "data": data
    })
    response = flask.make_response(resp_json_data, http_code)
    response.mimetype = "application/json"
    return response