from InnerLayers.DomainLayer.DomainModels.Comment import Comment
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID


class CommentRepository:
    def save(self, questionID: UUID, answerID: UUID, comment: Comment):
        pass

    def fetch(self, filteredByQuestionIDs: list, filteredByAnswerIDs: list, filteredByUUIDs: list, filteredByTime: list,
              filteredByVote: list, filteredByStatuses: list):
        pass

    def update(self, newComment: Comment):
        pass

    def delete(self, commentID: UUID):
        pass