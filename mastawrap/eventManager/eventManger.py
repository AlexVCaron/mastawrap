
class MetaEventManager(type):
    events = {}
    def __getitem__(self, item):
        return self.events[item] if item in self.events else None

class EventManager(metaclass=MetaEventManager):



    @classmethod
    def createTranslationEvent(cls, translation):
        cls._addEvent("translation", translation)

    def _addEvent(self, section, event):
        self._getSection(section).append(event)

    def _getSection(self, section):
        return EventManager[section]