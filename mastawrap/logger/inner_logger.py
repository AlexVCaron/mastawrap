from datetime import datetime
from tzlocal import get_localzone
import pytz


# LOGGING METACLASS
#   Serve the purpose of storing the Loggers and calling them with []
class MetaLogger(type):
    # Collection of all loggers
    _LOG_BOOK = {}

    def __setitem__(self, key, value):
        if not key in self._LOG_BOOK:
            self._LOG_BOOK[key] = value
        else:
            pass
            # TODO: A Logger merge is possible ???

    # Returns a logger => Usage : Logger["name"]
    def __getitem__(self, item):
        return self._LOG_BOOK[item] if item in self._LOG_BOOK else None


# Class defining a log entity.
#   This class is used to create log lines with timestamp.
# TODO : expand and add files to log entity to make it a complete Log Object that can log itself. (AGENT in log instead)
class Log:
    # @param time_regex: a string to format the timestamp of the log, one I love => "[{}]=> "
    # @param time_format: a string to humanize Epoch time, as formatted by strftime()
    #                     https://www.tutorialspoint.com/python/time_strftime.htm
    # @param log_line_format : a string to format a line in a log file (=timestamp + line_to_log)
    def __init__(self, log_line_format="{} : {}", time_regex="{}", time_format="%M/%d/%Y=%H:%M:%S.%f%z"):
        self._tr = time_regex
        self._tf = time_format
        self._lf = log_line_format

    def create_unit(self, block):
        return "{}".format(self._lf).format(self._create_timestamp(), block)

    def _create_timestamp(self):
        return self._tr.format(self._current_time())

    def _current_time(self):
        return datetime.now(pytz.utc).astimezone(get_localzone()).strftime(self._tf)
