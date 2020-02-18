import os
import requests
from flask import request
import craft_response

class Dispatch:

    def __init__(self):
        self.craft = craft_response.CraftResponse()


    def dispatch_requests(self, req, reqType):
        if reqType == "link":
            text = request.form['text']
            body = {"url": text, "country": "CA"}
            r = requests.post('https://songwhip.com/api/', json=body)
            return self.craft.get_links(r.json())
        if reqType == "init":
            return self.craft.init_response()

        return "We do not support this type of event"
