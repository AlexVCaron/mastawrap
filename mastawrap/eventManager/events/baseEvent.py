from enum import Enum


class BASE_EVENT_STATES(Enum):
    BASE = None


class BaseEvent:

    def __init__(self, descr, stateEnum=BASE_EVENT_STATES):
        self.states = stateEnum
        self._fillDescriptionAtInit(descr)

    def __getitem__(self, item):
        return self.descr[item] if item in self.descr else None

    def __contains__(self, item):
        return True if item in self.descr else False

    def _addCallback(self, callback, state):
        if state in self["callbacks"]:
            self["callbacks"][state].append(callback)
        else:
            self["callbacks"][state] = [callback]

    def _addPayload(self, load, uuid, unique=False):
        payload = {
            "unique": unique,
            "load": None if unique else list()
        } if uuid not in self["payload"] else self["payload"][uuid]
        if payload["unique"]:
            payload["load"] = load
        else:
            payload["load"].append(load)
        self.descr["payload"][uuid] = payload

    def _fillDescriptionAtInit(self, descr):
        for key, val in descr.items():
            if key in self:
                self.__getattribute__("_addK"+key)(val)
            else:
                self.descr[key] = val

    def _addKname(self, name):
        self.descr["name"] = name

    def _addKstate(self, state):
        self.descr["state"] = self.states[state.name]

    def _addKmessage(self, message):
        self.descr["message"] = message

    def _addKcallbacks(self, callbacks):
        for key, val in callbacks.items():
            self._addCallback(val, key)

    def _addKpayload(self, payloads):
        for key, val in payloads.items():
            self._addPayload(val["load"], key, val["unique"])

    descr = {
        "name": "base events",
        "state": BASE_EVENT_STATES["BASE"],
        "message": "",
        "callbacks": dict(),
        "payload": dict()
    }