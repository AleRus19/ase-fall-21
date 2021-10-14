from flakon import JsonBlueprint
from flask import Flask, request, jsonify

calc = JsonBlueprint('calc', __name__)


@calc.route('/calc/sum', methods=['GET'])
def sum():
    #http://127.0.0.1:5000/calc/sum?m=&n=
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    result = m
    add = 1 if n > 0 else -1  # add -1 if n is negative, 1 otherwise
    for _ in range(abs(n)):
        result += add
    return jsonify({'result': str(result)})


@calc.route('/calc/subtract', methods=['GET'])
def subtract():
    #http://127.0.0.1:5000/calc/subtract?m=&n=
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    result = m
    sub = -1 if n > 0 else 1
    for _ in range(abs(n)):
        result += sub
    return jsonify({'result': str(result)})


@calc.route('/calc/divide', methods=['GET'])
def divide():
    #http://127.0.0.1:5000/calc/divide?m=&n=
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

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
    return jsonify({'result': str(result)})


@calc.route('/calc/multiply', methods=['GET'])
def multiply():
    #http://127.0.0.1:5000/calc/multiply?m=&n=
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    negativeResult = (m > 0 and n < 0) or (m < 0 and n > 0)
    m = abs(m)
    n = abs(n)
    result = 0
    for _ in range(n):
        result += m
    result = -result if negativeResult else result
    return jsonify({'result': str(result)})
