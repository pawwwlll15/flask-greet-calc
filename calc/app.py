# Put your app in here.
from flask import Flask, request

app = Flask(__name__)

def get_requests():
    """return values of a and b requests"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return a,b

@app.route('/add')
def add():
    """add a and b"""
    a,b = get_requests()
    return f"the total is: {a + b}"

@app.route('/sub')
def sub():
    """subtract a and b"""

    a,b = get_requests()
    return f"the total is: {a - b}"

@app.route('/mult')
def mult():
    """multiply a and b"""

    a,b = get_requests()
    return f"the total is: {a * b}"

@app.route('/div')
def div():
    """divide a and b"""
    a,b = get_requests()
    return f"the total is: {a / b}"


operators = {'add':add,'sub':sub,'mult':mult,'div':div}

@app.route("/math/<oper>")
def math_page(oper):
    """ math operations on a and b"""
    result = operators[oper]()
    return result