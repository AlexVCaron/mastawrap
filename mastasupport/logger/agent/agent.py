from queue import Queue

from mastasupport.logger import Log


class _Agent:
    def __init__(self, log=Log(), queue=Queue()):
        self._queue = queue
        self._log = log

    def collect_log(self, log):
        self._queue.put_nowait(self._log.create_unit(log))

    def get_queue(self):
        tb = []
        while not self._queue.empty():
            tb.append(self._queue.get_nowait())
        return tb