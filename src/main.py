#!/bin/env python3

import logging as log

import json

from modules.config.reader import reader
from modules.database.database import database
from modules.utilities.utilities import utilities as util

if __name__ == '__main__':
    log.basicConfig(level=log.DEBUG)

    config_contents = reader.read_config()

    found, config_database = util.filter_config(config_contents, 'DATABASE')
    if not found:
        exit(1)

    ok, engine, session = database.create_session(config_database)
    ok = database.verify_contents(engine)