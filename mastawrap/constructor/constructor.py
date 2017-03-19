

class Constructor:
    """
    Classe de construction des composantes d'un langage de programmation.
    Tous les atomes et composantes du code passent par cette classe pour
    être construits soit dans le langage à traduire, soit dans le langage
    à généré. Aucun objet n'existe réellement à moins d'avoir besoin d'être
    utilisé.

    :param context Dictionnaire du contexte de l'application
    """

    instance = None

    def __init__(self, context):
        if not self.instance:
            self.instance = self.__Constructor(context)
        else:
            self.replaceContext(context)

    def replaceContext(self, context):
        self.instance.context = context

    class __Constructor:
        def __init__(self, context):
            self.context = context