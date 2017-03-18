from mastawrap.eventManager.metaEventManger import MetaEventManager


class EventManager(metaclass=MetaEventManager):

    def _addEvent(self, section, event):
        try:
            EventManager.getSection(section).append(event)
        except AttributeError:
            EventManager.createSection(section)
            self._addEvent(section, event)
