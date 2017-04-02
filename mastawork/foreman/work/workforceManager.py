from mastacore.resources.worker import Worker
from mastawork.base.resource import Resource


class WorkforceManager(Resource):

    workforce = dict()

    def __init__(self, context, spec):
        super().__init__(context)
        self._initSelfFromSpec(spec)

    def _initSelfFromSpec(self, spec):
        pass

    def enroll(self, count):
        for i in range(count):
            self.addWorker()

    def addWorker(self):
        wk = Worker.create()
        self.workforce[wk.uuid] = wk
