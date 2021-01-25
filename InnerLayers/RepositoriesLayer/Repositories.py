from InnerLayers.RepositoriesLayer.AnswerRepository import AnswerRepository
from InnerLayers.RepositoriesLayer.CommentRepository import CommentRepository
from InnerLayers.RepositoriesLayer.QuestionRepository import QuestionRepository
from InnerLayers.RepositoriesLayer.TagRepository import TagRepository


class Repositories:
    def __init__(self):
        self.questionRepository: QuestionRepository = None
        self.answerRepository: AnswerRepository = None
        self.commentRepository: CommentRepository = None
        self.tagRepository: TagRepository = None

    def initialize(self, questionRepository, answerRepository, commentRepository, tagRepository):
        self.questionRepository = questionRepository
        self.answerRepository = answerRepository
        self.commentRepository = commentRepository
        self.tagRepository = tagRepository
