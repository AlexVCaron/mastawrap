from queue import Queue

from mastawrap.logger.inner_logger import MetaLogger, Log

from mastasupport.logger.agent import _Agent

LOGGER_INIT_KWARGS = ["LOG"]

LOG_INIT_OBLIGATORY_KEYS = [""]


# LOGGING DECORATOR
#   This decorator logs the function call and its arguments and kwarguments
#   It then executes the function and logs the result if there is one. The
#   decorator is not exception-safe and will drag down all exceptions to the
#   caller without affecting the Stacktrace.
def logger(name):
    def func_logger(func):
        def args_logger(*args, **kwargs):
            Logger[name].log("{} called with | arguments {} | kwarguments {} |".format(func,
                                                                            args.__str__(),
                                                                            kwargs.__str__()))
            res = func(*args, **kwargs)
            if res:
                Logger[name].log("RESULT : {}".format(res))
            return res
        return args_logger
    return func_logger


# Class : Logger : unit which serves the purpose of logging things in a queue.
#                   the logger is collection oriented. You should never try to
#                   instanciate a logger directly, talking to its agent is way
#                   better.
class Logger(metaclass=MetaLogger):

    # Return name of a logger object
    def _get_name(self):
        return self._id
    name = property(_get_name)

    def __init__(self, name, **kwargs):
        self._agent = _Agent(Log(**kwargs), Queue())
        self._id = name
        Logger[name] = self

    def get_agent(self):
        return self._agent

    def log(self, log):
        self._agent.collect_log(log)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass










