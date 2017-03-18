from enum import Enum


class TranslationState(Enum):
    SUBMITTED="SUBMITTED",
    PENDING="PENDING",
    ASSIGNED="ASSIGNED",
    INPROGRESS="IN PROGRESS",
    CANCELED="CANCELED",
    PAUSED="PAUSED",
    SUCCESS="SUCCESS",
    ERROR="ERROR"


class TranslationEvent:
    descr = {
        "translation" : None,
        "state" : "",
        "message" : "",
        "callback": {TranslationState: []},
        "payload" : { }
    }

    def __init__(self, translation, descr):
        self.descr = descr
        self.descr["translation"] = translation

    def __getitem__(self, item):
        return self.descr[item] if item in self.descr else None

    def onSuccess(self, callback):
        self._addCallback(TranslationState.SUCCESS, callback)

    def onError(self, callback):
        self._addCallback(TranslationState.ERROR, callback)

    def onAssigned(self, callback):
        self._addCallback(TranslationState.ASSIGNED, callback)

    def _addCallback(self, callback, state):
        if self["callback"][state]:
            self["callback"][state].append(callback)
        else:
            self["callback"][state] = [callback]
