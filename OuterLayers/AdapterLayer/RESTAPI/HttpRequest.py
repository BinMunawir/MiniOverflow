
class HttpRequest:
    def __init__(self, method, path, pathParams=None, queryParams=None, headers=None, body=None):
        self.method = method
        self.path = path
        self.pathParams = pathParams
        self.queryParams = queryParams
        self.headers = headers
        self.body = body
