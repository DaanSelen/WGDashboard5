#!/bin/env python3

import logging as log

from .utilities import checks

class reader():
    @staticmethod
    def read_config() -> tuple[bool, dict]:
        '''
        check some basic things and then return the dict containing the config data
        '''

        ok, candidate_path = checks.search_known_paths()
        if not ok:
            return False, {}
        ok, config_contents = checks.verify_contents(candidate_path)
        if not ok:
            return False, {}

        return True, config_contents

    @staticmethod
    def refresh_config(config_contents: dict) -> dict:
        log.debug(f'refreshing config values')
        return reader.read_config()