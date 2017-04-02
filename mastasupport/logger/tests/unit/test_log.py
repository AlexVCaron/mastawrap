from datetime import datetime
from unittest import TestCase

from mastasupport.logger import Log


class TestLog(TestCase):
    def setUp(self):
        self.log_line_format="{}_{}"
        self.time_regex="[{}]"
        self.time_format="%f"
        self.log = Log(self.log_line_format, self.time_regex, self.time_format)

    def test_create_unit(self):
        log_line = "BLAHHH"
        tm = datetime.now().strftime(self.log_line_format.format(self.time_regex.format(self.time_format),
                                                                 log_line))
        tm2 = self.log.create_unit(log_line)
        self.assertEqual(tm, tm2)

    def test__create_timestamp(self):
        tm = datetime.now().strftime(self.time_regex.format(self.time_format))
        tm2 = self.log._create_timestamp()
        self.assertEqual(tm, tm2)

    def test__current_time(self):
        tm = datetime.now().strftime(self.time_format)
        tm2 = self.log._current_time()
        self.assertAlmostEqual(tm, tm2, delta=100)

