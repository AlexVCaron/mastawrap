import os

from mastawork.base.contextManager import ContextManager
from mastawork.base.resource import Resource
from mastasupport.utils.paths import get_base_path


class Library(Resource):

    def __init__(self, context):
        super().__init__(context)
        self._loadInterpreters()

    def _loadInterpreters(self):
        pth = get_base_path() + "\\interpreters"
        self.context = ContextManager.prepContextFor("library", self.context, {
            "available_interpreters": {
                "base_path": pth,
                "atoms": os.listdir(pth)
            }
        })
