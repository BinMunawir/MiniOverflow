
class HttpRequest:
    def __init__(self, pathParams={}, queryParams={}, headers={}, body={}):
        self.pathParams = pathParams
        self.queryParams = queryParams
        self.headers = headers
        self.body = body
