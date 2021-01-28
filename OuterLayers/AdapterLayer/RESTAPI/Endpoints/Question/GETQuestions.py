import json

from InnerLayers.UsecaseLayer.ApplicationUsecases.QuestionUsecases import getQuestions
from InnerLayers.UsecaseLayer.DataTrnsferObjects.QuestionDTO import QuestionDTO
from OuterLayers.AdapterLayer.RESTAPI.Endpoint import Endpoint
from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest
from OuterLayers.AdapterLayer.RESTAPI.HttpResponse import HttpResponse


class GETQuestions(Endpoint):
    method = "GET"
    path = "/api/questions"
    def __init__(self, request: HttpRequest):
        super(GETQuestions, self).__init__(request)

    def handle(self) -> HttpResponse:
        questionsMap = getQuestions()
        questionsMap = QuestionDTO.toListOfMap(questionsMap)
        for q in questionsMap:
            for i, a in enumerate(q['answers']):
                q['answers'][i] = a['answerID']
            for i, a in enumerate(q['comments']):
                q['comments'][i] = a['commentID']
        response: HttpResponse = HttpResponse(200, {'Content-Type': 'application/json'}, json.dumps(questionsMap))
        return response
