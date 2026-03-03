#!/bin/env python3

import flask

def make_resp_obj(success: bool = True, message: str = "", data: dict = {}, http_code: int = 200) -> flask.wrappers.Response:
    response = flask.make_response({
        "status": success,
        "message": message,
        "data": data
    }, http_code
    )

    return response