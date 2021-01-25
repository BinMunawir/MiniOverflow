
from InnerLayers.RepositoriesLayer.Repositories import Repositories
from InnerLayers.UsecaseLayer.DataTrnsferObjects.CommentDTO import CommentDTO
from InnerLayers.UsecaseLayer.services.Authentication import Authentication
from InnerLayers.UsecaseLayer.services.UUIDGenerator import UUIDGenerator


def getAllOfQuestion(db: Repositories, commentDTO: CommentDTO):
    return db.commentRepository.fetch([commentDTO.questionID])


def getAllOfAnswer(db: Repositories, commentDTO: CommentDTO):
    return db.commentRepository.fetch(filteredByAnswerIDs=[commentDTO.answerID])

