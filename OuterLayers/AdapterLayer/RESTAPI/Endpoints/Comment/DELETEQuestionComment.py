import json

from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.UsecaseLayer.ApplicationUsecases.CommentUsecases import deleteComment
from OuterLayers.AdapterLayer.RESTAPI.Endpoint import Endpoint
from OuterLayers.AdapterLayer.RESTAPI.Endpoints.Exception import HttpException
from OuterLayers.AdapterLayer.RESTAPI.HttpRequest import HttpRequest
from OuterLayers.AdapterLayer.RESTAPI.HttpResponse import HttpResponse


class DELETEQuestionComment(Endpoint):
    method = "DELETE"
    path = "/api/questions/:questionID/comments/:commentID"

    def __init__(self, request: HttpRequest):
        super(DELETEQuestionComment, self).__init__(request)

    def handle(self) -> HttpResponse:
        try:
            commentID = self.request.pathParams['commentID']
        except Exception as e:
            raise HttpException(1111, 'commentID is required')

        deleteComment(UUID(commentID))

        return HttpResponse(200, None, None)
