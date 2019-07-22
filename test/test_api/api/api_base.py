import requests
from test.test_api.base import APIUtils

class APIBase(APIUtils):

    def __init__(self, *args, **kwargs):
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])
        self.url = "https://platform.rescale.com/api/v2"
