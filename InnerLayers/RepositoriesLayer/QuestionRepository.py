
from InnerLayers.DomainLayer.DomainModels.Question import Question
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID


class QuestionRepository:
    def save(self, question: Question):
        pass

    def fetch(self, filteredByUUIDs: list, filteredByTitles: list, filteredByTime: list, filteredByVote: list,
              filteredByStatuses: list, filteredByAnswered: list, filteredByTags: list):
        pass

    def update(self, newQuestion: Question):
        pass

    def delete(self, questionID: UUID):
        pass
