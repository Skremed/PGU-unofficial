import time
import logging


def setup_logging() -> None:
    """Setting up the logging object"""
    # get local time
    t = time.localtime()
    # setup logging
    logging.basicConfig(filename=f"{t[0]}-{t[1]}-{t[2]}.log",
    format='[%(asctime)s] - [%(levelname)s] -> %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG
    )
    return None