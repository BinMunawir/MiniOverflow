import json
import time
from datetime import datetime

from InnerLayers.DomainLayer.DomainModels.Comment import Comment
from InnerLayers.RepositoriesLayer.Repositories import Repositories
from InnerLayers.UsecaseLayer.DataTrnsferObjects.QuestionDTO import QuestionDTO
from InnerLayers.UsecaseLayer.Services.Services import Services
from OuterLayers.AdapterLayer.InternalServices.UUIDModel import UUIDModel
from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest
from OuterLayers.AdapterLayer.RESTAPI.HttpResponse import HttpResponse
from OuterLayers.AdapterLayer.RESTAPI.Routes import router
from OuterLayers.InfrastructureLayer import InMemoryDB
from OuterLayers.InfrastructureLayer.InMemoryDB.AnswersDB import AnswersDB
from OuterLayers.InfrastructureLayer.InMemoryDB.CommentsDB import CommentsDB
from OuterLayers.InfrastructureLayer.InMemoryDB.QuestionsDB import QuestionsDB


qr = QuestionsDB()
ar = AnswersDB()
cr = CommentsDB()
Repositories.initialize(qr, ar, cr, None)
uuidModel = UUIDModel()
Services.initialize(uuidModel, None)


request = HttpRequest("POST", 'api/questions')
request.body = {'title': 'q1 title', 'body': 'q1 body'}
response = router(request)
print(999, response.body)
request = HttpRequest("GET", 'api/questions')
response = router(request)
print(999, response.body)
request = HttpRequest("GET", 'api/questions/:questionID')
questionID = {'questionID': json.loads(response.body)[0]['questionID']}
request.pathParams = questionID
response = router(request)
print(999, response.body)
request = HttpRequest("GET", 'api/questions')
response = router(request)
print(999, response.body)
request = HttpRequest("DELETE", 'api/questions/:questionID')
request.pathParams = questionID
response = router(request)
print(999, response.body)
request = HttpRequest("GET", 'api/questions/')
response = router(request)
print(999, response.body)
request = HttpRequest("POST", 'api/questions/:questionID/answers')
request.pathParams = questionID
request.body = {'body': 'answer1 body for question 1'}
response = router(request)
print(999, response.body)
request = HttpRequest("GET", 'api/questions/:questionID/answers')
request.pathParams = questionID
response = router(request)
print(999, response.body)
request = HttpRequest("DELETE", 'api/questions/:questionID/answers/:answerID')
answerID = {'answerID': json.loads(response.body)[0]['answerID']}
request.pathParams = answerID
response = router(request)
print(999, response.body)
request = HttpRequest("GET", 'api/questions/:questionID/answers')
request.pathParams = questionID
response = router(request)
print(999, response.body)
request = HttpRequest("POST", 'api/questions/:questionID/comments')
request.pathParams = questionID
request.body = {'body': 'comment1 body for question 1'}
response = router(request)
print(999, response.body)
request = HttpRequest("POST", 'api/questions/:questionID/answers/:answerID/comments')
request.pathParams = answerID
request.body = {'body': 'comment1 body for answer 1'}
response = router(request)
print(999, response.body)
request = HttpRequest("GET", 'api/questions/:questionID/comments')
request.pathParams = questionID
response = router(request)
print(999, response.body)
request = HttpRequest("GET", 'api/questions/:questionID/answers/:answerID/comments')
request.pathParams = answerID
response = router(request)
print(999, response.body)
# print(888, cr.db)






# test InMemoryDB
# commentDB = CommentsDB()
# comment = Comment('123', 'hello')
# commentDB.insert(99, None, comment)
# commentDB.delete('123')
# print(commentDB.questionComments)
