from unittest import TestCase

from mock import MagicMock

from mastasupport.logger.agent import _Agent


class Test_Agent(TestCase):
    def setUp(self):
        self.fake_log = MagicMock()
        self.fake_queue = MagicMock()
        self.agent = _Agent(self.fake_log, self.fake_queue)

    def test_collect_log(self):
        fake_log = "BLAHHH"
        fake_log_return = "____BLAHHH____"

        self.fake_log.create_unit.return_value = fake_log_return

        self.agent.collect_log(fake_log)

        self.fake_log.create_unit.assert_called_once_with(fake_log)
        self.fake_queue.put_nowait.assert_called_once_with(fake_log_return)

    def test_get_queue_empty(self):
        queue = self.agent.get_queue()

        self.assertCountEqual(queue, [])

    def test_get_queue_items(self):
        fake_log = "BLAHHH"
        fake_log_return = "____BLAHHH____"

        self.fake_log.create_unit.return_value = fake_log_return
        self.fake_queue.get_nowait.return_value = fake_log_return

        self.agent.collect_log(fake_log)
        self.agent.collect_log(fake_log)
        self.agent.collect_log(fake_log)

        empty_mock = MagicMock()
        empty_mock.side_effect = [False, False, False, True]
        self.fake_queue.empty = empty_mock

        queue = self.agent.get_queue()

        self.assertEqual(self.fake_log.create_unit.call_count, 3)
        self.assertEqual(self.fake_queue.put_nowait.call_count, 3)
        self.assertEqual(self.fake_queue.get_nowait.call_count, 3)
        self.assertEqual(empty_mock.call_count, 4)

        self.assertEqual(len(queue), 3)
        for it in queue:
            self.assertEqual(it, fake_log_return)
