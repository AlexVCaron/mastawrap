from mastawrap.eventManager.eventManger import EventManager


class TranslationEventManager(EventManager):

    def createTranslationEvent(self, translation):
        self._addEvent("translation", translation)
