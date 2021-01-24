from InnerLayers.DomainLayer.DomainSpecificLanguage.Status import Status


class AnswerStatus(Status):

    def __init__(self, name):
        super(AnswerStatus, self).__init__(name)

    def isPending(self):
        return self.NAME == AnswerStatus.PENDING().NAME
    def isDeleted(self):
        return self.NAME == AnswerStatus.DELETED().NAME
    def isActive(self):
        return self.NAME == AnswerStatus.ACTIVE().NAME

    @staticmethod
    def PENDING(): return AnswerStatus('PENDING')
    @staticmethod
    def DELETED(): return AnswerStatus('DELETED')
    @staticmethod
    def ACTIVE(): return AnswerStatus('ACTIVE')
