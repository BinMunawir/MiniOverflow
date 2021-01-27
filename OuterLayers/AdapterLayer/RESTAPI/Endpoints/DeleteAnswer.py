import json

from InnerLayers.UsecaseLayer.ApplicationUsecases.AnswerUsecases import softDeleteAnswer
from InnerLayers.UsecaseLayer.DataTrnsferObjects.AnswerDTO import AnswerDTO
from OuterLayers.AdapterLayer.RESTAPI.Endpoint import Endpoint
from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest
from OuterLayers.AdapterLayer.RESTAPI.HttpResponse import HttpResponse


class DeleteAnswer(Endpoint):
    def __init__(self, request: HttpRequest):
        super(DeleteAnswer, self).__init__(request)

    def handle(self) -> HttpResponse:
        response: HttpResponse = HttpResponse()
        softDeleteAnswer(self.request.pathParams['answerID'])
        response.status = 200
        return response
