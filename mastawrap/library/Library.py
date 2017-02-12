from mastawrap.base.resource import Resource
from mastawrap.base.utils.utils import get_base_path
from mastawrap.base.utils.contextManager.contextManager import ContextManager
import os


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
