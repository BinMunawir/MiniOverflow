from InnerLayers.DomainLayer.DomainModels.Question import Question
from InnerLayers.DomainLayer.DomainSpecificLanguage.QuestionStatus import QuestionStatus
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.RepositoriesLayer.Repositories import Repositories
from InnerLayers.UsecaseLayer.DataTrnsferObjects.QuestionDTO import QuestionDTO
from InnerLayers.UsecaseLayer.Services.Services import Services


def askQuestion(questionDTO: QuestionDTO) -> None:
    uuid = Services.uuidGenerator.generate()
    question = Question(uuid, questionDTO.title, questionDTO.body, questionDTO.tags)
    Repositories.questionRepository.save(question)


def getQuestions() -> list:
    questions: list = Repositories.questionRepository.fetch()
    return QuestionDTO.toListOfDTO(questions)


def getQuestion(questionID: UUID) -> QuestionDTO:
    question: list = Repositories.questionRepository.fetch(filteredByUUIDs=[questionID])[0]
    return QuestionDTO.toDTO(question)


def softDeleteQuestion(questionID: UUID) -> None:
    question: Question = Repositories.questionRepository.fetch(filteredByUUIDs=[questionID])[0]
    question.changeStatus(QuestionStatus.DELETED())
    Repositories.questionRepository.update(question)
