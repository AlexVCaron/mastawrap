from copy import deepcopy

from mastawrap.constructor.constructorEvents.translationEvent import TranslationEvent


class TranslationEventTemplate:

    def __init__(self, descr):
        self.descr = descr

    def fillAndFetch(self, translation):
        descr = deepcopy(self.descr)
        descr["translation"] = translation
        return TranslationEvent(descr)