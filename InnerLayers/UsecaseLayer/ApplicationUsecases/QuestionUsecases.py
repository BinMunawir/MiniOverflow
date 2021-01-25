
from InnerLayers.DomainLayer.DomainModels.Question import Question
from InnerLayers.DomainLayer.DomainSpecificLanguage.QuestionStatus import QuestionStatus
from InnerLayers.RepositoriesLayer.Repositories import Repositories
from InnerLayers.UsecaseLayer.DataTrnsferObjects.QuestionDTO import QuestionDTO
from InnerLayers.UsecaseLayer.services.Authentication import Authentication
from InnerLayers.UsecaseLayer.services.Services import Services
from InnerLayers.UsecaseLayer.services.UUIDGenerator import UUIDGenerator


def getAll(db: Repositories):
    return db.questionRepository.fetch()


def create(db: Repositories, questionDTO: QuestionDTO) -> None:
    # Services().authentication().authenticate('userToken')
    uuid = Services().uuidGenerator.generate()
    question = Question(uuid, questionDTO.title, questionDTO.body, questionDTO.tags)
    db.questionRepository.insert(question)


def softDelete(db: Repositories, questionDTO: QuestionDTO) -> None:
    question: Question = db.questionRepository.fetch([questionDTO.questionID])[0]
    question.changeStatus(QuestionStatus.DELETED())
    db.questionRepository.update(question)


def hardDelete(db: Repositories, questionDTO: QuestionDTO) -> None:
    # implemented inefficiently
    db.questionRepository.delete(questionDTO.questionID)
    answers: [] = db.answerRepository.fetch([questionDTO.questionID])
    for a in answers:
        pass  # hard delete answer
    comments: [] = db.commentRepository.fetch([questionDTO.questionID])
    for a in comments:
        pass  # hard delete comment
