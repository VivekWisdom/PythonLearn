""" Calculating Fibonacci Number series using Class """
#! usr/bin/python

class Fibonacci():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def series(self):
        while True:
            yield self.b
            self.a, self.b = self.b, self.a + self.b

F = Fibonacci(0, 1)
for n in F.series():
    if n > 100:
        break
    print(n)
