from InnerLayers.DomainLayer.DomainModels.Answer import Answer
from InnerLayers.DomainLayer.DomainModels.Question import Question
from InnerLayers.DomainLayer.DomainSpecificLanguage.BestAnswer import BestAnswer
from InnerLayers.DomainLayer.DomainSpecificLanguage.Body import Body
from InnerLayers.DomainLayer.DomainSpecificLanguage.QuestionStatus import QuestionStatus
from InnerLayers.DomainLayer.DomainSpecificLanguage.Time import Time
from InnerLayers.DomainLayer.DomainSpecificLanguage.Title import Title
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.DomainLayer.DomainSpecificLanguage.Vote import Vote
from InnerLayers.RepositoriesLayer.QuestionRepository import QuestionRepository
from InnerLayers.RepositoriesLayer.Repositories import Repositories
from InnerLayers.UsecaseLayer.DataTrnsferObjects.QuestionDTO import QuestionDTO
from InnerLayers.UsecaseLayer.DataTrnsferObjects.TagDTO import TagDTO
from OuterLayers.InfrastructureLayer.InMemoryDB.AnswersDB import AnswersDB


class QuestionsDB(QuestionRepository):
    def __init__(self):
        self.db = []

    def save(self, question: Question):
        questionMap = QuestionDTO.toDTO(question).toMap()
        if 'answers' in questionMap:
            for i, a in enumerate(questionMap['answers']):
                questionMap['answers'][i] = a['answerID']
        if 'comments' in questionMap:
            for i, a in enumerate(questionMap['comments']):
                questionMap['comments'][i] = a['commentID']
        self.db.append(questionMap)



    def fetch(self, filteredByUUIDs: list = None, filteredByTitles: list = None, filteredByTime: list = None,
              filteredByVote: list = None, filteredByStatuses: list = None, filteredByAnswered: list = None,
              filteredByTags: list = None):
        data = []
        if filteredByUUIDs is not None:
            for uuid in filteredByUUIDs:
                for q in self.db:
                    if uuid.toRepresent() == q['questionID']:
                        data.append(q)
        else:
            data = self.db
        result = []
        for q in data:
            answers = Repositories.answerRepository.fetch(filteredByUUIDs=q['answers']) if 'answers' in q else None
            comments = Repositories.commentRepository.fetch(filteredByUUIDs=q['comments']) if 'comments' in q else None
            # tags = Repositories.tagRepository.fetch(filteredByUUIDs=q['tags']) if 'tags' in q else None
            question = Question(
                questionID=UUID(q['questionID']) if 'questionID' in q else None,
                title=Title(q['title']) if 'title' in q else None,
                body=Body(q['body']) if 'body' in q else None,
                createdAt=Time(q['createdAt']) if 'createdAt' in q else None,
                votes=Vote(q['votes']) if 'votes' in q else None,
                bestAnswer=BestAnswer(q['bestAnswer']) if 'bestAnswer' in q else None,
                status=QuestionStatus(q['status']) if 'status' in q else None,
                comments=comments,
                tags=None,
                answers=answers,
            )
            result.append(question)
        return result

    def update(self, newQuestion: Question):
        for q in self.db:
            if q['questionID'] == newQuestion.questionID.toRepresent():
                self.delete(newQuestion.questionID)
                self.save(newQuestion)
                return

    def delete(self, questionID: UUID):
        for q in self.db:
            if q['questionID'] == questionID.UUID:
                self.db.remove(q)
                return
