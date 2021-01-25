from InnerLayers.DomainLayer.DomainModels.Comment import Comment
from InnerLayers.RepositoriesLayer.Repositories import Repositories
from InnerLayers.UsecaseLayer.DataTrnsferObjects.CommentDTO import CommentDTO
from InnerLayers.UsecaseLayer.services.Authentication import Authentication
from InnerLayers.UsecaseLayer.services.Services import Services
from InnerLayers.UsecaseLayer.services.UUIDGenerator import UUIDGenerator


def getAllOfQuestion(db: Repositories, commentDTO: CommentDTO):
    return db.commentRepository.fetch([commentDTO.questionID])


def getAllOfAnswer(db: Repositories, commentDTO: CommentDTO):
    return db.commentRepository.fetch(filteredByAnswerIDs=[commentDTO.answerID])


def commentOnQuestion(db: Repositories, commentDTO: CommentDTO) -> None:
    uuid = Services().uuidGenerator.generate()
    comment = Comment(uuid, commentDTO.body)
    db.commentRepository.insert(commentDTO.questionID, None, comment)


def commentOnAnswer(db: Repositories, commentDTO: CommentDTO) -> None:
    uuid = Services().uuidGenerator.generate()
    comment = Comment(uuid, commentDTO.body)
    db.commentRepository.insert(None, commentDTO.answerID, comment)


def delete(db: Repositories, commentDTO: CommentDTO) -> None:
    db.commentRepository.delete(commentDTO.commentID)
