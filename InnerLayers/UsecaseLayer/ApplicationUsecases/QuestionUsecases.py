from InnerLayers.DomainLayer.DomainModels.Answer import Answer
from InnerLayers.DomainLayer.DomainModels.Comment import Comment
from InnerLayers.DomainLayer.DomainModels.Question import Question
from InnerLayers.DomainLayer.DomainSpecificLanguage.QuestionStatus import QuestionStatus
from InnerLayers.DomainLayer.DomainSpecificLanguage.Time import Time
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.DomainLayer.DomainSpecificLanguage.Vote import Vote
from InnerLayers.RepositoriesLayer.Repositories import Repositories
from InnerLayers.UsecaseLayer.ApplicationUsecases.AnswerUsecases import hardDeleteAnswer
from InnerLayers.UsecaseLayer.ApplicationUsecases.CommentUsecases import deleteComment
from InnerLayers.UsecaseLayer.DataTrnsferObjects.QuestionDTO import QuestionDTO
from InnerLayers.UsecaseLayer.Services.Services import Services


def askQuestion(questionDTO: QuestionDTO) -> None:
    uuid = Services.uuidGenerator.generate()
    question = Question(questionID=uuid,
                        title=questionDTO.title,
                        body=questionDTO.body,
                        createdAt=Time(),
                        votes=Vote(0),
                        tags=questionDTO.tags if questionDTO.tags else [],
                        bestAnswer=None,
                        status=QuestionStatus.PENDING(),
                        comments=questionDTO.comments if questionDTO.comments else [],
                        answers=questionDTO.answers if questionDTO.answers else [])
    Repositories.questionRepository.save(question)


def getQuestions() -> list:
    questions: list = Repositories.questionRepository.fetch()
    return QuestionDTO.toListOfDTO(questions)


def getQuestion(questionID: UUID) -> QuestionDTO:
    question: list = Repositories.questionRepository.fetch(filteredByUUIDs=[questionID])
    if len(question) == 0: return None
    return QuestionDTO.toDTO(question[0])


def softDeleteQuestion(questionID: UUID) -> None:
    question: Question = Repositories.questionRepository.fetch(filteredByUUIDs=[questionID])[0]
    question.changeStatus(QuestionStatus.DELETED())
    Repositories.questionRepository.update(question)


def hardDeleteQuestion(questionID: UUID) -> None:
    question: Question = Repositories.questionRepository.fetch(filteredByUUIDs=[questionID])
    answers: list = question.answers
    for e in answers:
        a: Answer = e
        hardDeleteAnswer(a.answerID)
    comments: list = question.comments
    for e in comments:
        c: Comment = e
        deleteComment(c.commentID)
    Repositories.questionRepository.delete(questionID)