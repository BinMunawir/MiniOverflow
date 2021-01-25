
from InnerLayers.DomainLayer.DomainModels.Answer import Answer
from InnerLayers.DomainLayer.DomainSpecificLanguage.AnswerStatus import AnswerStatus
from InnerLayers.RepositoriesLayer.Repositories import Repositories
from InnerLayers.UsecaseLayer.DataTrnsferObjects.AnswerDTO import AnswerDTO
from InnerLayers.UsecaseLayer.services.Services import Services


def getAll(db: Repositories):
    return db.answerRepository.fetch()


def create(db: Repositories, answerDTO: AnswerDTO) -> None:
    # Authentication().authenticate('userToken')
    uuid = Services().uuidGenerator.generate()
    answer = Answer(uuid, answerDTO.body)
    db.answerRepository.insert(answer)


def softDelete(db: Repositories, answerDTO: AnswerDTO) -> None:
    answer: Answer = db.answerRepository.fetch([answerDTO.answerID])[0]
    answer.changeStatus(AnswerStatus.DELETED())
    db.answerRepository.update(answer)


def hardDelete(db: Repositories, answerDTO: AnswerDTO) -> None:
    # implemented inefficiently
    db.answerRepository.delete(answerDTO.answerID)
    comments: [] = db.commentRepository.fetch(filteredByAnswerIDs=[answerDTO.answerID])
    for c in comments:
        pass  # hard delete comment
