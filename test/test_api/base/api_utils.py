from requests import Request
import pdb

class APIUtils(object):

    _session_timeout = 10

    def __init__(self, *args, **kwargs):
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])

    def _send_request(self, url, http_verb, files = None, *args, **kwargs):
        options = {
            "verify": True,
            "allow_redirects": False,
            "timeout": self._session_timeout
        }
        if not files:
            files = {}
        options.update(kwargs)
        request_method = getattr(self.session, http_verb)
        response = request_method(url, files = files, **options)
        response.raise_for_status()
        return response

    def get(self, url, *args, **kwargs):
        return self._send_request(url, "get", *args, **kwargs)

    def post(self, url, *args, **kwargs):
        return self._send_request(url, "post", *args, **kwargs)

    def response_content(self, response):
        response_content = None
        try:
            return response.json()
        except ValueError:
            response_content = response.text
        return response_content
