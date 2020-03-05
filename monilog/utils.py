'''
Utility functions for the monitoring and log generation.
'''

import time
import logging


def init_logger():
    '''
    Initialise the logger.

    Returns:
        logger (Logger): Logger to use for the monitoring.
    '''

    log_format = '%(asctime)s %(levelname)s %(message)s'

    logger = logging.getLogger('Log monitoring console')
    logger.setLevel(logging.INFO)

    fh = logging.FileHandler(
        'simulation-'+time.strftime('%d-%b-%Y-%H:%M:%S')+'.log'
    )
    fh.setLevel(logging.INFO)

    formatter = logging.Formatter(log_format)
    fh.setFormatter(formatter)

    logger.addHandler(fh)

    return logger
