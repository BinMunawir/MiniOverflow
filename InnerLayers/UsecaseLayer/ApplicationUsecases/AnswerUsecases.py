from InnerLayers.DomainLayer.DomainModels.Answer import Answer
from InnerLayers.DomainLayer.DomainSpecificLanguage.AnswerStatus import AnswerStatus
from InnerLayers.RepositoriesLayer.Repositories import Repositories
from InnerLayers.UsecaseLayer.DataTrnsferObjects.AnswerDTO import AnswerDTO
from InnerLayers.UsecaseLayer.services.Authentication import Authentication
from InnerLayers.UsecaseLayer.services.UUIDGenerator import UUIDGenerator


def getAll(db: Repositories):
    return db.answerRepository.fetch()


def create(db: Repositories, answerDTO: AnswerDTO) -> None:
    # Authentication().authenticate('userToken')
    uuid = UUIDGenerator().generate()
    answer = Answer(uuid, answerDTO.body)
    db.answerRepository.insert(answer)


def softDelete(db: Repositories, answerDTO: AnswerDTO) -> None:
    answer: Answer = db.answerRepository.fetch([answerDTO.answerID])[0]
    answer.changeStatus(AnswerStatus.DELETED())
    db.answerRepository.update(answer)
