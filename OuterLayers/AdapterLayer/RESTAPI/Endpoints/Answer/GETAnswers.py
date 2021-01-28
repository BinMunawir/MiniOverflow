import json

from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.UsecaseLayer.ApplicationUsecases.AnswerUsecases import getAnswersOfQuestion
from InnerLayers.UsecaseLayer.ApplicationUsecases.QuestionUsecases import getQuestions
from InnerLayers.UsecaseLayer.DataTrnsferObjects.AnswerDTO import AnswerDTO
from InnerLayers.UsecaseLayer.DataTrnsferObjects.QuestionDTO import QuestionDTO
from OuterLayers.AdapterLayer.RESTAPI.Endpoint import Endpoint
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.Exception import HttpException
from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest
from OuterLayers.AdapterLayer.RESTAPI.HttpResponse import HttpResponse


class GETAnswers(Endpoint):
    method = "GET"
    path = "/api/questions/:questionID/answers"

    def __init__(self, request: HttpRequest):
        super(GETAnswers, self).__init__(request)

    def handle(self) -> HttpResponse:
        try:
            questionID = self.request.pathParams['questionID']
        except Exception as e:
            raise HttpException(1111, 'questionID are required')

        answers = getAnswersOfQuestion(UUID(questionID))
        answersMap = AnswerDTO.toListOfMap(answers)

        response: HttpResponse = HttpResponse(200, {'Content-Type': 'application/json'}, json.dumps(answersMap))
        return response
