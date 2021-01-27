import json

from OuterLayers.AdapterLayer.RESTAPI.Endpoints.AnswerQuestion import AnswerQuestion
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.AskQuestion import AskQuestion
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.DeleteAnswer import DeleteAnswer
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.GetAnswersOfQuestion import GetAnswersOfQuestion
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.GetQuestion import GetQuestion
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.GetQuestions import GetQuestions
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.DeleteQuestion import DeleteQuestion
from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest
from OuterLayers.AdapterLayer.RESTAPI.HttpResponse import HttpResponse


def router(request: HttpRequest) -> HttpResponse:
    if request.path[0] != '/': request.path = '/'+request.path
    if request.path[-1] != '/': request.path = request.path+'/'

    if request.method == "GET" and request.path == "/api/questions/":
        endpoint: GetQuestions = GetQuestions(request)
        response = endpoint.handle()
        return response
    if request.method == "GET" and request.path == "/api/questions/:questionID/":
        endpoint: GetQuestion = GetQuestion(request)
        response = endpoint.handle()
        return response
    if request.method == "POST" and request.path == "/api/questions/":
        endpoint: AskQuestion = AskQuestion(request)
        response = endpoint.handle()
        return response
    if request.method == "DELETE" and request.path == "/api/questions/:questionID/":
        endpoint: DeleteQuestion = DeleteQuestion(request)
        response = endpoint.handle()
        return response
    if request.method == "POST" and request.path == "/api/questions/:questionID/answers/":
        endpoint = AnswerQuestion(request)
        response = endpoint.handle()
        return response
    if request.method == "GET" and request.path == "/api/questions/:questionID/answers/":
        endpoint = GetAnswersOfQuestion(request)
        response = endpoint.handle()
        return response
    if request.method == "DELETE" and request.path == "/api/questions/:questionID/answers/:answerID/":
        endpoint = DeleteAnswer(request)
        response = endpoint.handle()
        return response
    return HttpResponse(404, {'Content-Type': 'application/json'}, json.dumps({'code': 1111, 'msg': 'Source Not Found'}))

