from uuid import uuid4, NAMESPACE_OID, uuid5

from mastasupport.exceptions.exceptions import RegisteredUUIDException
from mastasupport.utils.prop import prop


class metaUUID(type):
    uuids = prop(set)

    def __contains__(self, item):
        return True if item in self.uuids else False

    def additem(self, value):
        self.uuids.add(value)
        return value


class UUID(metaclass=metaUUID):
    @classmethod
    def generateUnique(cls):
        uuid = uuid4().hex
        uuid = UUID.generateUnique() if uuid in UUID else UUID.additem(uuid)
        return uuid

    @classmethod
    def generateFromBase(cls, base, namespace=NAMESPACE_OID):
        uuid = uuid5(namespace, base).hex
        if uuid not in UUID:
            UUID.additem(uuid)
        else:
            raise RegisteredUUIDException("UUID registered", uuid, base)
        return uuid