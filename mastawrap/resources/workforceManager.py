from mastawrap.resources.base import BaseResource, BaseResourceQuery


class WorkforceManager(BaseResource):

    @classmethod
    def query(cls, spec):
        return WorkforceManagerQuery(spec)

    @classmethod
    def create(cls, count):
        pass


class WorkforceManagerQuery(BaseResourceQuery):
    pass
