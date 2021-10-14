# calculator.py

def sum(m, n):
    ''' Increment n times the value of m.
        Return the value of m after the increment.
    '''
    result = m
    add = 1 if n > 0 else -1  # add -1 if n is negative, 1 otherwise
    for _ in range(abs(n)):
        result += add
    return result


def subtract(m, n):
    ''' Decrement n times the value of m. 
        Return the value of m after the decrement.
    '''
    result = m
    sub = -1 if n > 0 else 1
    for _ in range(abs(n)):
        result += sub
    return result


def divide(m, n):
    ''' Subtrac n from m until m gets to 0.
        Return the number of substraction.
    '''
    if n == 0:
        raise ZeroDivisionError('You cannot divide by 0')
    result = 0
    # decide the sign of the result
    negativeResult = (m > 0 and n < 0) or (m < 0 and n > 0)
    n = abs(n)
    m = abs(m)
    while (m - n >= 0):
        m -= n
        result += 1
    result = -result if negativeResult else result
    return result


def multiply(m, n):
    ''' Sum the value of m for n times.
        Return the sum.
    '''
    # decide the sign of the result
    negativeResult = (m > 0 and n < 0) or (m < 0 and n > 0)
    m = abs(m)
    n = abs(n)
    result = 0
    for _ in range(n):
        result += m
    result = -result if negativeResult else result
    return result


def gcd(m, n):
    ''' Return the greatest common divisor of the two integers'''
    while n != 0:
        r = m % n
        m = n
        n = r
    return abs(m)
