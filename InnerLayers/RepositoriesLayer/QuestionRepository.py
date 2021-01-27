
from InnerLayers.DomainLayer.DomainModels.Question import Question
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID


class QuestionRepository:
    def save(self, question: Question):
        pass

    def fetch(self, filteredByUUIDs: list = None, filteredByTitles: list = None, filteredByTime: list = None,
              filteredByVote: list = None, filteredByStatuses: list = None, filteredByAnswered: list = None,
              filteredByTags: list = None):
        pass

    def update(self, newQuestion: Question):
        pass

    def delete(self, questionID: UUID):
        pass
