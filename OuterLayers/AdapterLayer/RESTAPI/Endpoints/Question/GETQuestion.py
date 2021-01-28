import json

from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.UsecaseLayer.ApplicationUsecases.QuestionUsecases import getQuestions, getQuestion
from InnerLayers.UsecaseLayer.DataTrnsferObjects.QuestionDTO import QuestionDTO
from OuterLayers.AdapterLayer.RESTAPI.Endpoint import Endpoint
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.Exception import HttpException
from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest
from OuterLayers.AdapterLayer.RESTAPI.HttpResponse import HttpResponse


class GETQuestion(Endpoint):
    method = "GET"
    path = "/api/questions/:questionID"

    def __init__(self, request: HttpRequest):
        super(GETQuestion, self).__init__(request)

    def handle(self) -> HttpResponse:
        try:
            questionID = self.request.pathParams['questionID']
        except Exception as e:
            raise HttpException(1111, 'questionID is required')

        questionsMap = getQuestion(UUID(questionID))
        questionsMap = QuestionDTO.toMap(questionsMap)

        for i, a in enumerate(questionsMap['answers']):
            questionsMap['answers'][i] = a['answerID']
        for i, a in enumerate(questionsMap['comments']):
            questionsMap['comments'][i] = a['commentID']
        response: HttpResponse = HttpResponse(200, {'Content-Type': 'application/json'}, json.dumps(questionsMap))
        return response
