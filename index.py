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
from OuterLayers.InfrastructureLayer.InMemoryDB.QuestionsDB import QuestionsDB


qr = QuestionsDB()
Repositories.initialize(qr, None, None, None)
uuidModel = UUIDModel()
Services.initialize(uuidModel, None)

request = HttpRequest("POST", 'api/questions')
request.body = {'title': 'q1 title', 'body': 'q1 body'}
response = router(request)
print(888, response.body)
request = HttpRequest("GET", 'api/questions')
response = router(request)
print(999, response.body)

# request = HttpRequest("GET", '/api/questions/')
# response: HttpResponse = router(request)
# print(response.body)







# test InMemoryDB
# commentDB = CommentsDB()
# comment = Comment('123', 'hello')
# commentDB.insert(99, None, comment)
# commentDB.delete('123')
# print(commentDB.questionComments)
