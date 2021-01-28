import json

from InnerLayers.DomainLayer.DomainSpecificLanguage.Body import Body
from InnerLayers.DomainLayer.DomainSpecificLanguage.Title import Title
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.UsecaseLayer.ApplicationUsecases.AnswerUsecases import answerQuestion
from InnerLayers.UsecaseLayer.ApplicationUsecases.QuestionUsecases import askQuestion
from InnerLayers.UsecaseLayer.DataTrnsferObjects.AnswerDTO import AnswerDTO
from InnerLayers.UsecaseLayer.DataTrnsferObjects.QuestionDTO import QuestionDTO
from OuterLayers.AdapterLayer.RESTAPI.Endpoint import Endpoint
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.Exception import HttpException
from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest
from OuterLayers.AdapterLayer.RESTAPI.HttpResponse import HttpResponse


class POSTAnswer(Endpoint):
    method = "POST"
    path = "/api/questions/:questionID/answers"

    def __init__(self, request: HttpRequest):
        super(POSTAnswer, self).__init__(request)

    def handle(self) -> HttpResponse:

        try:
            questionID = self.request.pathParams['questionID']
            answerDTO = AnswerDTO()
            answerDTO.body = Body(self.request.body['body'])
        except Exception as e:
            raise HttpException(1111, 'questionID and body are required')

        answerQuestion(UUID(questionID), answerDTO)

        return HttpResponse(200, None, None)
