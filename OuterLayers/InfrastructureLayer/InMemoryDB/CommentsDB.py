from InnerLayers.DomainLayer.DomainModels.Comment import Comment
from InnerLayers.DomainLayer.DomainSpecificLanguage.Body import Body
from InnerLayers.DomainLayer.DomainSpecificLanguage.CommentStatus import CommentStatus
from InnerLayers.DomainLayer.DomainSpecificLanguage.Time import Time
from InnerLayers.DomainLayer.DomainSpecificLanguage.Title import Title
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.DomainLayer.DomainSpecificLanguage.Vote import Vote
from InnerLayers.RepositoriesLayer.CommentRepository import CommentRepository
from InnerLayers.UsecaseLayer.DataTrnsferObjects.CommentDTO import CommentDTO
from InnerLayers.UsecaseLayer.DataTrnsferObjects.TagDTO import TagDTO




class CommentsDB(CommentRepository):
    def __init__(self):
        self.db = []

    def save(self, questionID: UUID, answerID: UUID, comment: Comment):
        data = CommentDTO.toDTO(comment).toMap()
        if questionID is not None:
            data.update({'questionID': questionID.UUID})
        if answerID is not None:
            data.update({'answerID': answerID.UUID})
        self.db.append(data)

    def fetch(self, filteredByQuestionIDs: list = None, filteredByAnswerIDs: list = None, filteredByUUIDs: list = None,
              filteredByTime: list = None, filteredByVote: list = None, filteredByStatuses: list = None):
        data = []
        if filteredByUUIDs is not None:
            for uuid in filteredByUUIDs:
                for c in self.db:
                    if uuid == c['commentID']:
                        data.append(c)
        elif filteredByQuestionIDs is not None:
            for uuid in filteredByQuestionIDs:
                for c in self.db:
                    if 'questionID' in c and uuid.toRepresent() == c['questionID']:
                        data.append(c)
        elif filteredByAnswerIDs is not None:
            for uuid in filteredByAnswerIDs:
                for c in self.db:
                    if 'answerID' in c and uuid.toRepresent() == c['answerID']:
                        data.append(c)
        else:
            data = self.db
        result = []
        for c in data:
            result.append(Comment(
                commentID=UUID(c['commentID']) if 'commentID' in c else None,
                body=Body(c['body']) if 'body' in c else None,
                createdAt=Time(c['createdAt']) if 'createdAt' in c else None,
                status=CommentStatus(c['status']) if 'status' in c else None,
            ))
        return result

    def update(self, newComment: Comment):
        for c in self.db:
            if c['commentID'] == newComment.commentID.UUID:
                self.delete(newComment.commentID)
                if c['questionID'] is not None:
                    self.save(UUID(c['questionID']), None, newComment)
                if c['answerID'] is not None:
                    self.save(None, UUID(c['answerID']), newComment)
                return

    def delete(self, commentID: UUID):
        for c in self.db:
            if c['commentID'] == commentID.UUID:
                self.db.remove(c)
                return
