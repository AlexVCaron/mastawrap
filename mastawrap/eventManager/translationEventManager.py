from mastawrap.eventManager.eventManager import EventManager
from mastawrap.eventManager.eventTemplateManager import require_template


class TranslationEventManager(EventManager):

    @require_template("translation")
    def createTranslationEvent(self, templateId, translation):
        self._addEvent("translation", translation)
