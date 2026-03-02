#!/bin/env python3

import logging as log

import os
from urllib.parse import quote_plus

from modules.utilities.utilities import utilities as util

class checks():
    '''
    This class functions as a collection of function to prepare a connection to a database.
    '''

    @staticmethod
    def generate_connection_string(database_config: dict) -> tuple[bool, str]:
        if not 'type' in database_config:
            return False, ''

        username = quote_plus(database_config.get('username', ''))
        password = quote_plus(database_config.get('password', ''))

        match database_config['type']:
            case 'sqlite':
                local_database_path = os.path.abspath("./database")

                exists = util.ensure_directory(local_database_path)
                if exists:
                    connection_string = f'sqlite:///{local_database_path}/wgdashboard.db'
                else:
                    return False, ''

            case 'postgresql' | 'postgres':
                connection_string = f'postgresql+psycopg://{username}:{password}@{database_config.get('host', 'localhost')}:{database_config.get('port', '5432')}'

            case 'mariadb':
                connection_string = f'mariadb+mariadbconnector://{username}:{password}@{database_config.get('host', 'localhost')}:{database_config.get('port', '3306')}'

            case 'mysql':
                connection_string = f'mysql+pymysql://{username}:{password}@{database_config.get('host', 'localhost')}:{database_config.get('port', '3306')}'

            case _:
                return False, ''

        return True, connection_string