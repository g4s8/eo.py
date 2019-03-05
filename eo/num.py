"""
Number objects
"""

from eo import lang


class _Sum(lang.EO):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __value__(self):
        return int(self.left) + int(self.right)


class _Neg(lang.EO):
    def __init__(self, val):
        self.val = val

    def __value__(self):
        return -self.val


class _Mul(lang.EO):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __value__(self):
        return float(self.left) * float(self.right)


assert _Mul(3, 4) == 12
assert _Sum(1, 2) == 3
assert _Neg(4) == -4

Neg = _Neg(0)
Sum = _Sum(0, 0)
Mul = _Mul(0, 0)
