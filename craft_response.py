

class CraftResponse:

    def __init__(self):
        self.response = ""

    def get_links(self, data):
        print(data)
        fields = data['data']
        artist = fields['artists'][0]
        album_name = fields['name']
        self.response += "The Linked Album is {} by {}".format(artist['name'], album_name)
        return self.response