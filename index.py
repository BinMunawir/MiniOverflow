import json

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

from InnerLayers.RepositoriesLayer.Repositories import Repositories
from InnerLayers.UsecaseLayer.Services.Services import Services
from OuterLayers.AdapterLayer.InternalServices.UUIDModel import UUIDModel
from OuterLayers.AdapterLayer.RESTAPI import Router
from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest
from OuterLayers.AdapterLayer.RESTAPI.Router import router
from OuterLayers.InfrastructureLayer.InMemoryDB.AnswersDB import AnswersDB
from OuterLayers.InfrastructureLayer.InMemoryDB.CommentsDB import CommentsDB
from OuterLayers.InfrastructureLayer.InMemoryDB.QuestionsDB import QuestionsDB

qr = QuestionsDB()
ar = AnswersDB()
cr = CommentsDB()
Repositories.initialize(qr, ar, cr, None)
uuidModel = UUIDModel()
Services.initialize(uuidModel, None)


def djangoInputs(req: WSGIRequest, questionID, answerID, commentID):
    request = HttpRequest()
    request.headers = {}
    request.body = {}

    if 'title' in req.POST: request.body['title'] = req.POST['title']
    if 'body' in req.POST: request.body['body'] = req.POST['body']
    if questionID is not None:
        request.pathParams['questionID'] = questionID
        req.path = str(req.path).replace(str(questionID), ':questionID')
    if answerID is not None:
        request.pathParams['answerID'] = answerID
        req.path = str(req.path).replace(str(answerID), ':answerID')
    if commentID is not None:
        request.pathParams['commentID'] = commentID
        req.path = str(req.path).replace(str(commentID), ':commentID')
    if req.method == 'DELETE' and req.headers.get('hard') is not None: request.headers['hard'] = 'yes'

    response = router(req.method, req.path, request)
    res = HttpResponse(status=response.status,
                       content_type='application/json',
                       content=response.body if response.body is not None else {}
                       )
    return res


def runEndpoints():
    request = HttpRequest(body={'title': 't', 'body': 'b'})
    response = router("POST", '/api/questions', request)
    print(response.status, response.body)
    response = router("GET", '/api/questions', request)
    print(response.status, response.body)
    questionID = {'questionID': json.loads(response.body)[0]['questionID']}
    request.pathParams = questionID
    response = router("GET", '/api/questions/:questionID', request)
    print(response.status, response.body)
    response = router("DELETE", '/api/questions/:questionID', request)
    print(response.status, response.body)

    request = HttpRequest(body={'body': 'b'})
    request.pathParams = questionID
    response = router("POST", '/api/questions/:questionID/answers', request)
    print(response.status, response.body)
    response = router("GET", '/api/questions/:questionID/answers', request)
    print(response.status, response.body)
    answerID = {'answerID': json.loads(response.body)[0]['answerID']}
    request.pathParams = answerID
    response = router("DELETE", '/api/questions/:questionID/answers/:answerID', request)
    print(response.status, response.body)

    request = HttpRequest(body={'body': 'b'})
    request.pathParams = questionID
    response = router("POST", '/api/questions/:questionID/comments', request)
    print(response.status, response.body)
    request = HttpRequest(body={'body': 'b'})
    request.pathParams = answerID
    response = router("POST", '/api/questions/:questionID/answers/:answerID/comments', request)
    print(response.status, response.body)
    request.pathParams = questionID
    response = router("GET", '/api/questions/:questionID/comments', request)
    print(response.status, response.body)
    commentID2 = {'commentID': json.loads(response.body)[0]['commentID']}
    request.pathParams = answerID
    response = router("GET", '/api/questions/:questionID/answers/:answerID/comments', request)
    print(response.status, response.body)

    commentID = {'commentID': json.loads(response.body)[0]['commentID']}
    request.pathParams = commentID
    response = router("DELETE", '/api/questions/:questionID/comments/:commentID', request)
    print(response.status, response.body)
    request.pathParams = commentID2
    response = router("DELETE", '/api/questions/:questionID/answers/:answerID/comments/:commentID', request)
    print(response.status, response.body)
    request.headers['hard'] = ''
    request.pathParams = answerID
    response = router("DELETE", '/api/questions/:questionID/answers/:answerID', request)
    print(response.status, response.body)
    request.headers['hard'] = ''
    request.pathParams = questionID
    response = router("DELETE", '/api/questions/:questionID', request)
    print(response.status, response.body)

    print()
    print(len(qr.db))
    print(len(ar.db))
    print(len(cr.db))
