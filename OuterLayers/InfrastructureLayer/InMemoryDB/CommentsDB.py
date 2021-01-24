from InnerLayers.RepositoriesLayer.CommentRepository import CommentRepository


class CommentsDB(CommentRepository):

    def __init__(self):
        self.questionComments = []
        self.answerComments = []

    def insert(self, questionID, answerID, comment):
        if questionID:
            self.questionComments.append({'questionID': questionID, **comment.__dict__})
            return
        if answerID:
            self.answerComments.append([answerID, *comment])
            return

    def fetch(self, filteredByQuestionIDs, filteredByAnswerIDs, filteredByUUIDs, filteredByTime, filteredByVote,
              filteredByStatuses):
        return []

    def update(self, newBody, newStatus):
        pass

    def delete(self, commentID):
        for c in self.questionComments:
            if c['commentID'].UUID == commentID:
                self.questionComments.remove(c)
                return
        for c in self.answerComments:
            if c['commentID'].UUID == commentID:
                self.questionComments.remove(c)
                return

