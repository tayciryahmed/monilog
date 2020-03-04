import time
import logging


def init_logger():
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
