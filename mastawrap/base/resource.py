import inspect
import sys
from mastawrap.base.utils import contextManager

class Resource:
    def __init__(self, context):
        self.__context = context

    def populateContext(self, context):
        print(self)
        self.__context = context

    def _getContext(self):
        return self.__context

    def _setContext(self, context):
        self.__context = context

    context = property(_getContext, _setContext)