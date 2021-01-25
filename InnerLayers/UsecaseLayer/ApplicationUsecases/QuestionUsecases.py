from InnerLayers.DomainLayer.DomainModels.Question import Question
from InnerLayers.DomainLayer.DomainSpecificLanguage.QuestionStatus import QuestionStatus
from InnerLayers.RepositoriesLayer.QuestionRepository import QuestionRepository
from InnerLayers.RepositoriesLayer.Repositories import Repositories
from InnerLayers.UsecaseLayer.DataTrnsferObjects.QuestionDTO import QuestionDTO
from InnerLayers.UsecaseLayer.services.Authentication import Authentication
from InnerLayers.UsecaseLayer.services.UUIDGenerator import UUIDGenerator


def create(db: Repositories, questionDTO: QuestionDTO) -> None:
    # Authentication().authenticate('userToken')
    uuid = UUIDGenerator().generate()
    question = Question(uuid, questionDTO.title, questionDTO.body, questionDTO.tags)
    db.questionRepository.insert(question)



