from InnerLayers.DomainLayer.DomainModels.Answer import Answer
from InnerLayers.DomainLayer.DomainSpecificLanguage.AnswerStatus import AnswerStatus
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.RepositoriesLayer.Repositories import Repositories
from InnerLayers.UsecaseLayer.DataTrnsferObjects.AnswerDTO import AnswerDTO
from InnerLayers.UsecaseLayer.Services.Services import Services


def answerQuestion(questionID: UUID, answerDTO: AnswerDTO) -> None:
    uuid = Services.uuidGenerator.generate()
    answer = Answer(uuid, answerDTO.body)
    Repositories.answerRepository.save(questionID, answer)


def getAnswersOfQuestion(questionID: UUID) -> list:
    answers = Repositories.answerRepository.fetch(filteredByQuestionIDs=[questionID])
    return AnswerDTO.toListOfDTO(answers)


def softDeleteAnswer(answerID: UUID) -> None:
    answer: Answer = Repositories.answerRepository.fetch(filteredByUUIDs=[answerID])[0]
    answer.changeStatus(AnswerStatus.DELETED())
    Repositories.answerRepository.update(answer)
