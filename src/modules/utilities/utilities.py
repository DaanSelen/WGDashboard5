#!/bin/env python3

import logging as log

import os

class utilities():
    @staticmethod
    def filter_config(config_contents: dict, filter_keyword: str) -> tuple[bool, dict]:
        '''
        Helper function to grab a specific part of the config
        '''

        log.debug(f'searching for section: {filter_keyword}')
        for section in config_contents:
            if str(section).lower() == filter_keyword.lower():
                return True, dict(config_contents[section].items())

        return False, {}

    @staticmethod
    def ensure_directory(path: str) -> bool:
        '''
        Make the directory if it does not exist yet, return only true if the directory was missing and created.
        '''

        log.debug(f'checking if the directory at: {path} exists')
        if os.path.exists(path) and os.path.isdir(path):
            return True
        
        try:
            os.mkdir(path)
            return True

        except Exception as err:
            log.critical('failed to create directory')
            return False
        
        