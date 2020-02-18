import os
from flask import Flask, request
import dispatch
import requests

app = Flask(__name__)
        
dis = dispatch.Dispatch()

@app.route('/', methods=['POST'])
def init_app():
    print(request)
    return dis.dispatch_requests(request)
    # return {
    #     'token': "Yo8dkYH5HLme7rjo2DtB7mNl",
    #     'challenge': request.json['challenge'],
    #     'type': 'url_verification'
    # }

@app.route('/link', methods=['POST'])
def link_music():
    print(request.form)
    return dis.dispatch_requests(request, "link")

if __name__  == '__main__':
    app.run(host='0.0.0.0', debug=True)
