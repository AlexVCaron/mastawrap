from enum import Enum
from mastawrap.eventManager.events.baseEvent import BaseEvent


class TRANSLATION_EVENT_STATES(Enum):
    SUBMITTED="SUBMITTED",
    PENDING="PENDING",
    ASSIGNED="ASSIGNED",
    INPROGRESS="IN PROGRESS",
    CANCELED="CANCELED",
    PAUSED="PAUSED",
    SUCCESS="SUCCESS",
    ERROR="ERROR"


class TranslationEvent(BaseEvent):
    def __init__(self, descr):
        super().__init__(descr, TRANSLATION_EVENT_STATES)

    def onSuccess(self, callback):
        self._addCallback(TRANSLATION_EVENT_STATES.SUCCESS.name, callback)

    def onError(self, callback):
        self._addCallback(TRANSLATION_EVENT_STATES.ERROR.name, callback)

    def onAssigned(self, callback):
        self._addCallback(TRANSLATION_EVENT_STATES.ASSIGNED.name, callback)


