import json
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.GetQuestions import GetQuestions
from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest
from OuterLayers.AdapterLayer.RESTAPI.HttpResponse import HttpResponse

endpoints = [
]


def router(request: HttpRequest) -> HttpResponse:
    for e in endpoints:
        pass
    return HttpResponse(404, {'Content-Type': 'application/json'}, json.dumps({'code': 1111, 'msg': 'Source Not Found'}))

