from eo import *

class Fibonacci(EO):
    def __init__(self, n):
        self.n = n

    def __value__(self):
        return If(
            FirstIsLess(self.n, 2), 1,
            Sum(
                Fibonacci(Sum(self.n, Neg(1))),
                Fibonacci(Sum(self.n, Neg(2)))))


Printed(list(map(Fibonacci, range(0, 10)))).__value__()

assert Fibonacci(0) == 1
assert Fibonacci(1) == 1
assert Fibonacci(2) == 2
assert Fibonacci(3) == 3
assert Fibonacci(4) == 5
assert Fibonacci(5) == 8
