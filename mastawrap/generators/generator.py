
class Generator:
    def __init__(self, inCodeName, outCodeName):
        self.name = "".format(
            inCodeName,
            "->",
            outCodeName
        );

    class AtomTemplater:
        def __init__(self, fieldType):
            self.fieldType = fieldType

        def genDefinition(self, name, value="", **decorators):
            out = {
                'type': self.fieldType,
                'id': name,
                'value': value
            }
            if len(decorators) > 0:
                for dKey in decorators:
                    if dKey == "[TYPE]":
                        out['typeDecoration'] = str
                    elif dKey == "[ID]":
                        out['idDecoration'] = str
                    elif dKey == "[VALUE]":
                        out['valueDecoration'] = str
                    else:
                        str += decorators[dKey]

        def genDeclaration(self, ):
            pass