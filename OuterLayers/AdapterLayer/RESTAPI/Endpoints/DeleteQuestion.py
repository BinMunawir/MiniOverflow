import json

from InnerLayers.UsecaseLayer.ApplicationUsecases.QuestionUsecases import getQuestions, getQuestion, softDeleteQuestion
from InnerLayers.UsecaseLayer.DataTrnsferObjects.QuestionDTO import QuestionDTO
from OuterLayers.AdapterLayer.RESTAPI.Endpoint import Endpoint
from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest
from OuterLayers.AdapterLayer.RESTAPI.HttpResponse import HttpResponse


class DeleteQuestion(Endpoint):
    def __init__(self, request: HttpRequest):
        super(DeleteQuestion, self).__init__(request)

    def handle(self) -> HttpResponse:
        response: HttpResponse = HttpResponse()
        result = getQuestion(self.request.pathParams['questionID'])
        if result is None:
            response.status = 400
            response.headers = {'Content-Type': 'application/json'}
            response.body = json.dumps(
                {'code': 1111, 'msg': 'no question by that ID:'+self.request.pathParams['questionID']})
            return response
        softDeleteQuestion(self.request.pathParams['questionID'])
        response.status = 200
        return response
