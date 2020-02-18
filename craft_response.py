import os

class CraftResponse:

    def __init__(self):
        self.response = ""

    def get_links(self, data):
        fields = data['data']
        artist = fields['artists'][0]
        album_name = fields['name']
        links = fields['links']
        spotify = links['spotify'][0]['link']
        googleplay = links['googleplay'][0]['link']
        applemusic = self.format_apple_link(links['itunes'][0]['link'], "ca")
        self.response += "The Linked Album is {} by {}\n".format(artist['name'], album_name)
        self.response += "Spotify Link: {}\n".format(spotify)
        self.response += "Google Play Link: {}\n".format(googleplay)
        self.response += "Apple Music Link: {}\n".format(applemusic)
        return self.response

    def format_apple_link(self, link, country):
        pre = link.split("{")[0]
        post = link.split("}")[1]
        return pre + country + post

    def init_response(self):
        return {
            'token': os.environ.get('TOKEN'),
            'challenge': request.json['challenge'],
            'type': 'url_verification'
         }