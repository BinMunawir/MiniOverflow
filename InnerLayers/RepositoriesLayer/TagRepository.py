from InnerLayers.DomainLayer.DomainModels.Tag import Tag
from InnerLayers.DomainLayer.DomainSpecificLanguage.Name import Name
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID


class TagRepository:
    def save(self, tag: Tag):
        pass

    def update(self, newName: Name):
        pass

    def delete(self, tagID: UUID):
        pass
