from abc import ABCMeta, abstractmethod

from mastasupport.utils import prop


class BaseResource:
    @classmethod
    def query(cls, spec):
        pass

    @classmethod
    def create(cls, count=1):
        pass


class BaseResourceQuery(metaclass=ABCMeta):

    _context = prop(dict)
    _results = prop(list)

    def __init__(self, model):
        self._model = model
        self._results = self._fetch_corespondents()

    def contextual(self, context):
        self._context = context

    def findUnique(self):
        return self._model.readOut(self._results.first())

    @abstractmethod
    def _fetch_corespondents(self):
        pass
