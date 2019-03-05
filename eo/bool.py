"""
EO bool objects
"""

from eo import lang


class _Equals(lang.EO):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __value__(self):
        return self.left == self.right


class _Not(lang.EO):
    def __init__(self, val):
        self.val = val

    def __value__(self):
        return not self.val


class _If(lang.EO):
    def __init__(self, cond, succ, fallback=None):
        self.cond = cond
        self.succ = succ
        self.fallback = fallback

    def __value__(self):
        return self.succ if self.cond else self.fallback


class _FirstIsLess(lang.EO):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __value__(self):
        return int(self.left) < int(self.right)


class _FirstIsGreater(lang.EO):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __value__(self):
        return self.left > self.right


assert bool(_FirstIsLess(3, 4))
assert not bool(_FirstIsLess(5, 4))
assert not bool(_FirstIsLess(4, 4))
assert bool(_FirstIsGreater(4, 3))
assert not bool(_FirstIsGreater(3, 3))
assert not bool(_FirstIsGreater(2, 3))
assert bool(_Not(False))
assert _If(True, 1, 2) == 1
assert _If(False, 1, 2) == 2
assert _Equals(5, 5)

Equals = _Equals(True, False)
Not = _Not(True)
If = _If(False, None, None)
FirstIsLess = _FirstIsLess(0, 0)
FirstIsGreater = _FirstIsGreater(0, 0)
