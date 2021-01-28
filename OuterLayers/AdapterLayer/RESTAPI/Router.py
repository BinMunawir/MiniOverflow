import json

from OuterLayers.AdapterLayer.RESTAPI.Endpoints.Answer.DELETEAnswer import DELETEAnswer
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.Answer.GETAnswers import GETAnswers
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.Answer.POSTAnswer import POSTAnswer
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.AnswerQuestion import AnswerQuestion
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.Comment.DELETEAnswerComment import DELETEAnswerComment
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.Comment.DELETEQuestionComment import DELETEQuestionComment
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.Comment.GETAnswerComments import GETAnswerComments
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.Comment.GETQuestionComments import GETQuestionComments
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.Comment.POSTAnswerComment import POSTAnswerComment
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.Comment.POSTQuestionComment import POSTQuestionComment
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.Exception import HttpException
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.Question.DELETEQuestion import DELETEQuestion
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.Question.GETQuestion import GETQuestion
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.Question.GETQuestions import GETQuestions
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.Question.POSTQuestion import POSTQuestion
from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest
from OuterLayers.AdapterLayer.RESTAPI.HttpResponse import HttpResponse


def router(method, path, request: HttpRequest) -> HttpResponse:

    try:
        if method == POSTQuestion.method and path == POSTQuestion.path:
            return POSTQuestion(request).handle()
        if method == GETQuestions.method and path == GETQuestions.path:
            return GETQuestions(request).handle()
        if method == GETQuestion.method and path == GETQuestion.path:
            return GETQuestion(request).handle()
        if method == DELETEQuestion.method and path == DELETEQuestion.path:
            return DELETEQuestion(request).handle()
        if method == POSTAnswer.method and path == POSTAnswer.path:
            return POSTAnswer(request).handle()
        if method == DELETEAnswer.method and path == DELETEAnswer.path:
            return DELETEAnswer(request).handle()
        if method == GETAnswers.method and path == GETAnswers.path:
            return GETAnswers(request).handle()
        if method == POSTQuestionComment.method and path == POSTQuestionComment.path:
            return POSTQuestionComment(request).handle()
        if method == POSTAnswerComment.method and path == POSTAnswerComment.path:
            return POSTAnswerComment(request).handle()
        if method == GETQuestionComments.method and path == GETQuestionComments.path:
            return GETQuestionComments(request).handle()
        if method == GETAnswerComments.method and path == GETAnswerComments.path:
            return GETAnswerComments(request).handle()
        if method == DELETEQuestionComment.method and path == DELETEQuestionComment.path:
            return DELETEQuestionComment(request).handle()
        if method == DELETEAnswerComment.method and path == DELETEAnswerComment.path:
            return DELETEAnswerComment(request).handle()

    except HttpException as e:
        return HttpResponse(400, {'Content-Type': 'application/json'},
                            json.dumps({'code': e.code, 'msg': e.msg}))


    return HttpResponse(404, {'Content-Type': 'application/json'},
                        json.dumps({'code': 1111, 'msg': 'Source Not Found'}))
