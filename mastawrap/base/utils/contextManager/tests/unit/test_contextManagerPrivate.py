import json

from unittest import TestCase

from mastawrap.base.utils.contextManager.tests.unit import contextManagerTestHelper
from mastawrap.base.utils.utils import get_base_path



class TestContextManagerPrivate(TestCase):

    base_context = json.load(open(get_base_path() + "\\base\\utils\\contextManager\\baseContext.json"))

    def setUp(self):
        self.cMan = contextManagerTestHelper._construct_contextManager()

    def test__contexter(self):
        additions = {
            "dumb_add": "add_entry",
            "dumb_id": 6
        }

        mth = self.cMan.__getattribute__("_contexter")
        out = mth(self.cMan.context, additions)

        assert out["self"] is additions
        assert "parent" in out

    def test__constructSelfEntry(self):
        additions = {
            "dumb_add": "add_entry",
            "dumb_id": 6
        }

        mth = self.cMan.__getattribute__("_constructSelfEntry")
        entr = mth(additions, self.cMan.context)

        assert entr["self"] is additions
        assert entr["parent"] is self.cMan.context
