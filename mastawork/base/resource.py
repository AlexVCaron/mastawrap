from mastasupport.utils import prop


class Resource:
    def __init__(self, context):
        self.__context = context

    def populateContext(self, context):
        print(self)
        self.__context = context

    context = prop(dict)
