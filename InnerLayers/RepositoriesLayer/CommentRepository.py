

class CommentRepository:
    def insert(self, questionID, answerID, comment):
        pass

    def fetch(self, filteredByQuestionIDs, filteredByAnswerIDs, filteredByUUIDs, filteredByTime, filteredByVote,
                    filteredByStatuses):
        pass

    def update(self, newComment):
        pass

    def delete(self, commentID):
        pass