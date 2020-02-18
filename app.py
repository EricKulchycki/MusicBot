import os
from flask import Flask, request
import dispatch
import requests

class FlaskApp:

    app = Flask(__name__)
    
    def __init__(self):
        self.dis = dispatch.Dispatch()

    def start(self):
        self.app.run(host='0.0.0.0')

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
        text = request.form['text']
        body = {"url": text, "country": "CA"}
        r = requests.post('https://songwhip.com/api/', json=body)
        return r.json()


if __name__  == '__main__':
    flask = FlaskApp()
    flask.start()
