class QuestionRepository:
    def insert(self, question):
        pass

    def fetch(self, filteredByUUIDs, filteredByTitles, filteredByTime, filteredByVote, filteredByStatuses,
              filteredByAnswered, filteredByTags):
        pass

    def update(self, newTitle, newBody, newStatus, newTags):
        pass

    def delete(self, questionID):
        pass
