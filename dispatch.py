import os
from flask import request

class Dispatch:
    def dispatch_requests(self, req):
        body = req.json
        print(body)
        return body
