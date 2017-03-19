from mastawrap.resources.utils import prop


class BaseResourceModel:
    uuid = prop()

    def __init__(self, uuid):
        self.uuid = uuid


class WorkforceManagerModel(BaseResourceModel):
    name = prop()

    def __init__(self, name):
        self.name = name
