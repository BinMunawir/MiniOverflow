from InnerLayers.DomainLayer.DomainModels.Comment import Comment
from InnerLayers.DomainLayer.DomainSpecificLanguage.CommentStatus import CommentStatus
from InnerLayers.DomainLayer.DomainSpecificLanguage.Time import Time
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.RepositoriesLayer.Repositories import Repositories
from InnerLayers.UsecaseLayer.DataTrnsferObjects.CommentDTO import CommentDTO
from InnerLayers.UsecaseLayer.Services.Services import Services


def commentOnQuestion(questionID: UUID, commentDTO: CommentDTO) -> None:
    uuid = Services.uuidGenerator.generate()
    comment = Comment(commentID=uuid,
                      createdAt=Time(),
                      body=commentDTO.body,
                      status=CommentStatus.PENDING())
    Repositories.commentRepository.save(questionID, None, comment)


def commentOnAnswer(answerID: UUID, commentDTO: CommentDTO) -> None:
    uuid = Services.uuidGenerator.generate()
    comment = Comment(commentID=uuid,
                      createdAt=Time(),
                      body=commentDTO.body,
                      status=CommentStatus.PENDING())
    Repositories.commentRepository.save(None, answerID, comment)


def getQuestionComments(questionID: UUID) -> list:
    comments = Repositories.commentRepository.fetch(filteredByQuestionIDs=[questionID])
    return CommentDTO.toListOfDTO(comments)


def getAnswerComments(answerID: UUID) -> list:
    comments = Repositories.commentRepository.fetch(filteredByAnswerIDs=[answerID])
    return CommentDTO.toListOfDTO(comments)


def deleteComment(commentID: UUID) -> None:
    Repositories.commentRepository.delete(commentID)
