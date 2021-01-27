from InnerLayers.DomainLayer.DomainModels.Comment import Comment
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID


class CommentRepository:
    def save(self, questionID: UUID, answerID: UUID, comment: Comment):
        pass

    def fetch(self, filteredByQuestionIDs: list = None, filteredByAnswerIDs: list = None, filteredByUUIDs: list = None,
              filteredByTime: list = None, filteredByVote: list = None, filteredByStatuses: list = None):
        pass

    def update(self, newComment: Comment):
        pass

    def delete(self, commentID: UUID):
        pass