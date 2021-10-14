import calculator as c


class FooCalculator:
    ''' A class used to represent a basic calculator.'''

    # empty constructor
    def __init__(self):
        pass

    def sum(self, m, n):
        return c.sum(m, n)

    def subtract(self, m, n):
        return c.subtract(m, n)

    def divide(self, m, n):
        return c.divide(m, n)

    def multiply(self, m, n):
        return c.multiply(m, n)

    def gcd(self, m, n):
        return c.gcd(m, n)


if __name__ == '__main__':
    calc = FooCalculator()
    print(calc.gcd(16, 0))
