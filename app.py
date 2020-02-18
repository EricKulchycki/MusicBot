import os
from flask import Flask, request
import dispatch

class FlaskApp:

    app = Flask(__name__)

    def start(self):
        self.app.run(host='0.0.0.0')

    @app.route('/', methods=['POST'])
    def init_app():
        return dispatch.Dispatch().dispatch_requests(request)
        # return {
        #     'token': "Yo8dkYH5HLme7rjo2DtB7mNl",
        #     'challenge': request.json['challenge'],
        #     'type': 'url_verification'
        # }


if __name__  == '__main__':
    flask = FlaskApp()
    flask.start()
