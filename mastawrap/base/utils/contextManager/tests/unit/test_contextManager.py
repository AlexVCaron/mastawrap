from unittest import TestCase
from unittest import mock

from mastawrap.base.resource import Resource
from mastawrap.base.utils.contextManager.tests.unit import contextManagerTestHelper


class TestContextManager(TestCase):

    def setUp(self):
        self.cMan = contextManagerTestHelper._construct_contextManager()

    def test_replace_context(self):
        alt_context = {
            "alt_name": "alt_val",
            "alt_id": 9
        }
        rs = Resource(self.cMan.context)

        self.cMan.replace_context(rs, alt_context)

        for key in alt_context:
            assert rs.context[key] is alt_context[key]

    @mock.patch("mastawrap.base.utils.contextManager.contextManager.ContextManager._workerContexter", return_value={
            "alt_name": "alt_val",
            "alt_id": 9,
            "a": "b"
        })
    def test_prepContextFor(self, mck_cMan):
        alt_context = {
            "alt_name": "alt_val",
            "alt_id": 9
        }

        out = self.cMan.prepContextFor("worker", self.cMan.context, {"a": "b"})

        mck_cMan.assert_called_once_with(self.cMan.context, {"a": "b"})

        for key in alt_context:
            assert out[key] is alt_context[key]
        assert "a" in out


    @mock.patch("json.load", return_value="fresh")
    @mock.patch("mastawrap.base.resource.Resource")
    def test_populateWithBaseContext(self, rs, mck_lt):
        self.cMan.populateWithBaseContext(rs)

        rs.populateContext.assert_called_once_with("fresh")
