import os

class CraftResponse:

    def __init__(self):
        self.response = ""

    def get_links(self, data):
        self.response = ""
        fields = data['data']
        artist = fields['artists'][0]
        album_name = fields['name']
        links = fields['links']
        spotify = ''
        googleplay = ''
        applemusic = ''
        
        if 'spotify' in links:
            spotify = links['spotify'][0]['link']
        if 'googleplay' in links:
            googleplay = links['googleplay'][0]['link']
        if 'itunes' in links:
            applemusic = self.format_apple_link(links['itunes'][0]['link'], "ca")
        self.response += "The Linked Album is {} by {}\n".format(album_name, artist['name'])
        self.response += "Spotify Link: {}\n".format(spotify)
        self.response += "Google Play Link: {}\n".format(googleplay)
        self.response += "Apple Music Link: {}\n".format(applemusic)
        return { 'response_type': 'in_channel', 'text': self.response }

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
