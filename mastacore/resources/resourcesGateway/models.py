from mastasupport.utils import prop, UUID


class BaseResourceModel:
    uuid = prop(str)

    def __init__(self):
        self.uuid = UUID.generateUnique()

    def readOut(self, json_obj):
        fields = self.__class__.__dict__.keys()
        for field in fields:
            self.__setattr__(field, json_obj[field]) if field in json_obj else None


class WorkforceManagerModel(BaseResourceModel):
    name = prop(str)

    def __init__(self, name):
        self.name = name
        super().__init__()
