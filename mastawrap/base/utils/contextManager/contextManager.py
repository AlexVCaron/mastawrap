from mastawrap.base.resource import Resource
from mastawrap.base.utils.utils import load_from_template, get_base_path
from enum import Enum


class ObligatoryContextKeys(Enum):
    GLOBAL = "global"
    APP = "application"


class ContextManager(Resource):

    def __init__(self):
        super().__init__(dict)
        self.populateWithBaseContext(self)

    @classmethod
    def replace_context(cls, obj, context):
        obj.context = context

    @classmethod
    def prepContextFor(cls, entity="", baseContext=dict, additions=dict):
        contextPrepper = getattr(cls, "_" + entity + "Contexter")
        return contextPrepper(baseContext, additions)

    # TODO: utiliser la methode pour populer la base de l'application avec le contexte de départ
    @classmethod
    def populateWithBaseContext(cls, target):
        cpath = get_base_path() + "\\base\\utils\\contextManager\\baseContext.json"
        target.populateContext(load_from_template(cpath))

    # TODO: once this unit of contexter complexifies, create separate unit tests
    def _workerContexter(self, context=dict, additions=dict):
        return self._contexter(context, additions)

    def _farmerContexter(self, context=dict, additions=dict):
        return self._contexter(context, additions)

    def _libraryContexter(self, context=dict, additions=dict):
        return self._contexter(context, additions)

    def _contexter(self, context=dict, additions=dict):
        out = dict()

        for item in ObligatoryContextKeys:
            out[item.value] = context[item.value]

        if "self" in context:
            out.update(self._constructSelfEntry(additions, context["self"]))
        else:
            out.update(self._constructSelfEntry(additions, dict()))

        return out


    def _constructSelfEntry(self, ob, pa):
        return {
            "self": ob,
            "parent": pa
        }