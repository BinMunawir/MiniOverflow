import json

from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.RepositoriesLayer.Repositories import Repositories
from InnerLayers.UsecaseLayer.ApplicationUsecases.QuestionUsecases import getQuestions
from InnerLayers.UsecaseLayer.DataTrnsferObjects.QuestionDTO import QuestionDTO
from OuterLayers.AdapterLayer.RESTAPI.Endpoint import Endpoint
from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest
from OuterLayers.AdapterLayer.RESTAPI.HttpResponse import HttpResponse


class GetQuestions(Endpoint):
    def __init__(self, request: HttpRequest):
        super(GetQuestions, self).__init__(request)

    def handle(self) -> HttpResponse:
        result = getQuestions()
        result = QuestionDTO.toListOfMap(result)
        response: HttpResponse = HttpResponse({'Content-Type': 'application/json'}, json.dumps(result))
        return response
