# Put your app in here.
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def add():
    return "add works"