import requests

class APISession(object):

    def __init__(self, token):
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": "Token {}".format(token)
        })
