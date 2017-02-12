

import mock as mock

from unittest import TestCase

from mastawrap.logger.tests import helpers


class TestLoggerDecorator(TestCase):
    def setUp(self):
        self.name = "TestLoggerDecorator"
        self.logger = mock.MagicMock()
        self.logger[self.name] = self.logger

    def test_logger_decorator(self):
        with mock.patch('mastawrap.logger.inner_logger.MetaLogger.__getitem__') as get_logger_mock:
            get_logger_mock.return_value = self.logger

            helpers.test_logger_decorator(self.name)

            get_logger_mock.assert_called_with(self.name)
            self.logger.log.assert_called()
