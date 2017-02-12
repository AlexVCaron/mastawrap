from unittest import TestCase

from mock import MagicMock

from mastawrap.logger.logger import Logger


class TestLogger(TestCase):
    def setUp(self):
        self.name = "TestLogger"
        self.mock_agent = MagicMock()
        self.logger = Logger(self.name)
        self.logger._agent = self.mock_agent

    def test__get_name(self):
        name = self.logger.name
        assert name == self.name

    def test_get_agent(self):
        agent = self.logger.get_agent()
        self.assertEqual(agent, self.mock_agent)

    def test_log(self):
        fake_log = "BLAHHHHHH"
        self.logger.log(fake_log)
        self.mock_agent.collect_log.assert_called_with(fake_log)
