from InnerLayers.RepositoriesLayer.AnswerRepository import AnswerRepository
from InnerLayers.RepositoriesLayer.CommentRepository import CommentRepository
from InnerLayers.RepositoriesLayer.QuestionRepository import QuestionRepository
from InnerLayers.RepositoriesLayer.TagRepository import TagRepository


class Repositories:
    questionRepository: QuestionRepository = None
    answerRepository: AnswerRepository = None
    commentRepository: CommentRepository = None
    tagRepository: TagRepository = None

    @staticmethod
    def initialize(questionRepository, answerRepository, commentRepository, tagRepository):
        Repositories.questionRepository = questionRepository
        Repositories.answerRepository = answerRepository
        Repositories.commentRepository = commentRepository
        Repositories.tagRepository = tagRepository
