#!/usr/bin/python3
""" Calculating Fibonacci Number series using Class """


class Fibonacci(object):
    """ Class to generate Fibonacci Number series. """
    def __init__(self, a, b):
        self.a = a #Assign the passed value of constructor to object variable.
        self.b = b #Assign the passed value of constructor to object variable.
    def series(self):
        """ Code logic to generate Fibonacci Series """
        while True:
            yield self.b
            self.a, self.b = self.b, self.a + self.b

F = Fibonacci(0, 1)
for n in F.series(): # Generate all Fibonacci Numbers
    if n > 100: # Filter numbers greater than 100.
        break
    print(n)
