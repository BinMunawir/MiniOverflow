import json
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.GetQuestions import GetQuestions
from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest
from OuterLayers.AdapterLayer.RESTAPI.HttpResponse import HttpResponse


def router(request: HttpRequest) -> HttpResponse:
    if request.path[0] != '/': request.path = '/'+request.path
    if request.path[-1] != '/': request.path = request.path+'/'

    if request.method == "GET" and request.path == "/api/questions/":
        endpoint: GetQuestions = GetQuestions(request)
        response = endpoint.handle()
        return response
    return HttpResponse(404, {'Content-Type': 'application/json'}, json.dumps({'code': 1111, 'msg': 'Source Not Found'}))

