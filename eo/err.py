"""
Elegant errors
"""

from eo import lang


class _Failure(lang.EO, Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)

    def __value__(self):
        raise self


Failure = _Failure(None)
