from InnerLayers.DomainLayer.DomainSpecificLanguage.Status import Status


class CommentStatus(Status):

    def __init__(self, name):
        super(CommentStatus, self).__init__(name)

    def isPending(self):
        return self.NAME == CommentStatus.PENDING().NAME

    def isActive(self):
        return self.NAME == CommentStatus.ACTIVE().NAME

    @staticmethod
    def PENDING(): return CommentStatus('PENDING')
    @staticmethod
    def ACTIVE(): return CommentStatus('ACTIVE')
