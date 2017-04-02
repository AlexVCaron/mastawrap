import json
from unittest import mock

from mastawork.base.contextManager import ContextManager
from mastasupport.utils.paths import get_base_path

base_context = json.load(open(get_base_path() + "\\base\\utils\\contextManager\\baseContext.json"))


@mock.patch('json.load', return_value=base_context)
def _construct_contextManager(jsonload):
    cMan = ContextManager()
    cMan_context =cMan.context
    for key in base_context:
        assert cMan_context[key] is base_context[key]

    return cMan