class BaseResource:
    pass


class BaseResourceQuery:

    def __init__(self, sepc):
        self._sepc = sepc
        self.results = self._fetch_corespondents()

    def findUnique(self):
        return self.results.first()

    def _fetch_corespondents(self):
        pass
