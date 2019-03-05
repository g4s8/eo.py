"""
Console
"""

from eo import lang

class _Printed(lang.EO):
    def __init__(self, val):
        self.val = val

    def __value__(self):
        return print(self.val)

Printed = _Printed("")
