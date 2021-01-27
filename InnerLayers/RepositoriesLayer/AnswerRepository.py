from InnerLayers.DomainLayer.DomainModels.Answer import Answer
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID


class AnswerRepository:
    def save(self, questionID: UUID, answer: Answer):
        pass

    def fetch(self, filteredByQuestionIDs: list = None, filteredByUUIDs: list = None, filteredByTime: list = None,
              filteredByVote: list = None, filteredByStatuses: list = None):
        pass

    def update(self, newAnswer: Answer):
        pass

    def delete(self, answerID: UUID):
        pass
