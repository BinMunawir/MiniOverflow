from InnerLayers.DomainLayer.DomainModels.Comment import Comment
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.RepositoriesLayer.Repositories import Repositories
from InnerLayers.UsecaseLayer.DataTrnsferObjects.CommentDTO import CommentDTO
from InnerLayers.UsecaseLayer.Services.Services import Services


def commentOnQuestion(questionID: UUID, commentDTO: CommentDTO) -> None:
    uuid = Services.uuidGenerator.generate()
    comment = Comment(uuid, commentDTO.body)
    Repositories.commentRepository.save(questionID, None, comment)

def commentOnAnswer(answerID: UUID, commentDTO: CommentDTO) -> None:
    uuid = Services.uuidGenerator.generate()
    comment = Comment(uuid, commentDTO.body)
    Repositories.commentRepository.save(None, answerID, comment)
