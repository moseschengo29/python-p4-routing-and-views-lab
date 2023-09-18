#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'


@app.route('/count/<int:param>')
def count(param):
    numbers = '\n'.join(map(str, range(1, param + 1)))
    return f'<pre>{numbers}</pre>'

@app.route('/math/<float:num1><string:operation><float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Division by zero is not allowed!"
    elif operation == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return "Modulo by zero is not allowed!"
    
    if result is not None:
        return f'Result of {num1} {operation} {num2} is: {result}'
    else:
        return "Invalid operation or operands."

if __name__ == '__main__':
    app.run(port=5555, debug=True)
