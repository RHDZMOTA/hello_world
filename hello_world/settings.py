import os
import logging


HELLO_DEFAULT = os.environ.get(
    "HELLO_DEFAULT",
    default="World"
)


def get_logger(name: str):
    return logging.getLogger(name=name)
