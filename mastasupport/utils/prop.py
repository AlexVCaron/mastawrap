class prop(object):
    def __init__(self, type):
        self.val = type()

    def __get__(self, obj, objtype):
        return self.val

    def __set__(self, obj, val):
        self.val = val