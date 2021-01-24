from InnerLayers.DomainLayer.DomainSpecificLanguage.Status import Status


class QuestionStatus(Status):

    def __init__(self, name):
        super(QuestionStatus, self).__init__(name)

    def isPending(self):
        return self.NAME == QuestionStatus.PENDING().NAME
    def isDeleted(self):
        return self.NAME == QuestionStatus.DELETED().NAME
    def isActive(self):
        return self.NAME == QuestionStatus.ACTIVE().NAME
    def isClosed(self):
        return self.NAME == QuestionStatus.CLOSED().NAME

    @staticmethod
    def PENDING(): return QuestionStatus('PENDING')
    @staticmethod
    def DELETED(): return QuestionStatus('DELETED')
    @staticmethod
    def ACTIVE(): return QuestionStatus('ACTIVE')
    @staticmethod
    def CLOSED(): return QuestionStatus('CLOSED')
