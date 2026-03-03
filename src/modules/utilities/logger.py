#!/bin/env python3

from logging.config import dictConfig

@staticmethod
def setup_logger(level: str = 'DEBUG') -> None:
    dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] [%(levelname)s] in [%(module)s] %(message)s'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'level': level
            }
        },
        'root': {
            'handlers': ['console'],
            'level': level
        },
        'loggers': {
            'werkzeug': {  # make werkzeug logs match
                'handlers': ['console'],
                'level': level,
                'propagate': False
            },
            'flask.app': {  # make Flask internal logs match
                'handlers': ['console'],
                'level': level,
                'propagate': False
            }
        }
    })