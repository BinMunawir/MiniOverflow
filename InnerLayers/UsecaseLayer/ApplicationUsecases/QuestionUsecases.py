from InnerLayers.DomainLayer.DomainModels.Question import Question
from InnerLayers.RepositoriesLayer.Repositories import Repositories
from InnerLayers.UsecaseLayer.DataTrnsferObjects.QuestionDTO import QuestionDTO
from InnerLayers.UsecaseLayer.Services.Services import Services


def askQuestion(questionDTO: QuestionDTO) -> None:
    uuid = Services.uuidGenerator.generate()
    question = Question(uuid, questionDTO.title, questionDTO.body, questionDTO.tags)
    Repositories.questionRepository.save(question)
