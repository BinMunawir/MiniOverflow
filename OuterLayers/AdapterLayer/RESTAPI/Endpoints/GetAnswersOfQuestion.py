import json

from InnerLayers.DomainLayer.DomainSpecificLanguage.Body import Body
from InnerLayers.DomainLayer.DomainSpecificLanguage.Title import Title
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.RepositoriesLayer.Repositories import Repositories
from InnerLayers.UsecaseLayer.ApplicationUsecases.AnswerUsecases import answerQuestion, getAnswersOfQuestion
from InnerLayers.UsecaseLayer.ApplicationUsecases.QuestionUsecases import getQuestions, askQuestion
from InnerLayers.UsecaseLayer.DataTrnsferObjects.AnswerDTO import AnswerDTO
from InnerLayers.UsecaseLayer.DataTrnsferObjects.QuestionDTO import QuestionDTO
from OuterLayers.AdapterLayer.RESTAPI.Endpoint import Endpoint
from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest
from OuterLayers.AdapterLayer.RESTAPI.HttpResponse import HttpResponse


class GetAnswersOfQuestion(Endpoint):
    def __init__(self, request: HttpRequest):
        super(GetAnswersOfQuestion, self).__init__(request)

    def handle(self) -> HttpResponse:
        questionID = UUID(self.request.pathParams['questionID'])
        answers = getAnswersOfQuestion(questionID)
        answers = AnswerDTO.toListOfMap(answers)
        response: HttpResponse = HttpResponse(200, {'Content-Type': 'application/json'}, json.dumps(answers))
        return response
