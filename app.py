import os
from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
    print(request.body.token)
    return {
        'token': os.environ.get('TOKEN'),
        'challenge': request.body.token,
        'type': 'url_verification'
    }

if __name__  == '__main__':
    app.run(host='0.0.0.0')
