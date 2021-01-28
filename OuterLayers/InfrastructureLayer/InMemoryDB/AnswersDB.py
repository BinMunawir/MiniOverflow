from InnerLayers.DomainLayer.DomainModels.Answer import Answer
from InnerLayers.DomainLayer.DomainSpecificLanguage.BestAnswer import BestAnswer
from InnerLayers.DomainLayer.DomainSpecificLanguage.Body import Body
from InnerLayers.DomainLayer.DomainSpecificLanguage.AnswerStatus import AnswerStatus
from InnerLayers.DomainLayer.DomainSpecificLanguage.Time import Time
from InnerLayers.DomainLayer.DomainSpecificLanguage.Title import Title
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.DomainLayer.DomainSpecificLanguage.Vote import Vote
from InnerLayers.RepositoriesLayer.AnswerRepository import AnswerRepository
from InnerLayers.RepositoriesLayer.Repositories import Repositories
from InnerLayers.UsecaseLayer.DataTrnsferObjects.AnswerDTO import AnswerDTO
from InnerLayers.UsecaseLayer.DataTrnsferObjects.TagDTO import TagDTO


class AnswersDB(AnswerRepository):
    def __init__(self):
        self.db = []

    def save(self, questionID: UUID, answer: Answer):
        answerMap = AnswerDTO.toDTO(answer).toMap()
        answerMap.update({'questionID': questionID.UUID})
        if 'comments' in answerMap:
            for i, a in enumerate(answerMap['comments']):
                answerMap['comments'][i] = a['commentID']
        self.db.append(answerMap)

    def fetch(self, filteredByQuestionIDs: list = None, filteredByUUIDs: list = None, filteredByTime: list = None,
              filteredByVote: list = None, filteredByStatuses: list = None):
        data = []
        if filteredByUUIDs is not None:
            for uuid in filteredByUUIDs:
                if str(type(uuid)) == "<class 'str'>": uuid = UUID(uuid)
                for a in self.db:
                    if uuid.toRepresent() == a['answerID']:
                        data.append(a)
        elif filteredByQuestionIDs is not None:
            for uuid in filteredByQuestionIDs:
                if str(type(uuid)) == "<class 'str'>": uuid = UUID(uuid)
                for a in self.db:
                    if uuid.toRepresent() == a['questionID']:
                        data.append(a)
        else:
            data = self.db
        result = []
        for q in data:
            comments = Repositories.commentRepository.fetch(filteredByUUIDs=q['comments']) if 'comments' in q else None
            result.append(Answer(
                answerID=UUID(q['answerID']) if 'answerID' in q else None,
                body=Body(q['body']) if 'body' in q else None,
                createdAt=Time(q['createdAt']) if 'createdAt' in q else None,
                votes=Vote(q['votes']) if 'votes' in q else None,
                status=AnswerStatus(q['status']) if 'status' in q else None,
                comments=comments,
            ))
        return result

    def update(self, newAnswer: Answer):
        for a in self.db:
            if a['answerID'] == newAnswer.answerID.UUID:
                self.delete(newAnswer.answerID)
                self.save(UUID(a['questionID']), newAnswer)
                return

    def delete(self, answerID: UUID):
        for a in self.db:
            if a['answerID'] == answerID.UUID:
                self.db.remove(a)
                return
