import json

from InnerLayers.UsecaseLayer.ApplicationUsecases.QuestionUsecases import getQuestions, getQuestion
from InnerLayers.UsecaseLayer.DataTrnsferObjects.QuestionDTO import QuestionDTO
from OuterLayers.AdapterLayer.RESTAPI.Endpoint import Endpoint
from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest
from OuterLayers.AdapterLayer.RESTAPI.HttpResponse import HttpResponse


class GetQuestion(Endpoint):
    def __init__(self, request: HttpRequest):
        super(GetQuestion, self).__init__(request)

    def handle(self) -> HttpResponse:
        response: HttpResponse = HttpResponse(headers={'Content-Type': 'application/json'})
        result = getQuestion(self.request.pathParams['questionID'])
        if result is None:
            response.status = 400
            response.body = json.dumps(
                {'code': 1111, 'msg': 'no question by that ID:'+self.request.pathParams['questionID']})
            return response
        response.status = 200
        response.body = json.dumps(QuestionDTO.toMap(result))
        return response
