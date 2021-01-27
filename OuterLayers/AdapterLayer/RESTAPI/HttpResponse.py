
class HttpResponse:
    def __init__(self, status, headers, body):
        self.headers = headers
        self.body = body
        self.status = status
