from mastacore.resources.base import BaseResource, BaseResourceQuery


class WorkforceManager(BaseResource):

    @classmethod
    def query(cls, spec):
        return WorkforceManagerQuery(spec)


class WorkforceManagerQuery(BaseResourceQuery):
    pass
