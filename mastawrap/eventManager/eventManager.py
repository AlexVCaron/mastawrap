from mastawrap.eventManager.metaEventManager import MetaEventManager


class EventManager(metaclass=MetaEventManager):

    def __init__(self, section):
        self.section = EventManager.getSection(section)

    def _addEvent(self, event):
        self.section.append(event)
