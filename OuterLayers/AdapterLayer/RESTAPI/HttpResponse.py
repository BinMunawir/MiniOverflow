
class HttpResponse:
    def __init__(self, status=None, headers=None, body=None):
        self.headers = headers
        self.body = body
        self.status = status
