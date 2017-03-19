class RegisteredUUIDException(Exception):
    def __init__(self, message, uuid, name):
        super().__init__(message)
        self.uuid = uuid
        self.name = name