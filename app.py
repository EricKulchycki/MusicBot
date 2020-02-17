import os
from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['POST'])
def init_app():
    return {
        'token': "Yo8dkYH5HLme7rjo2DtB7mNl",
        'challenge': request.json['challenge'],
        'type': 'url_verification'
    }


if __name__  == '__main__':
    app.run(host='0.0.0.0')
