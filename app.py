import os
from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
    print(request)
    return "hey"

if __name__  == '__main__':
    app.run(host='0.0.0.0')
