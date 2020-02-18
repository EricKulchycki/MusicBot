import os
from flask import Flask, request
import dispatch

app = Flask(__name__)
        
dis = dispatch.Dispatch()

@app.route('/', methods=['POST'])
def init_app():
    return dis.dispatch_requests(request, "init")

@app.route('/link', methods=['POST'])
def link_music():
    return dis.dispatch_requests(request, "link")

if __name__  == '__main__':
    app.run(host='0.0.0.0', debug=True)
