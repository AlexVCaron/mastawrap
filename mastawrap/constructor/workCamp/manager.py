from mastawrap.base.resource import Resource
from mastawrap.base.utils.contextManager import ContextManager
from mastawrap.base.utils.utils import load_from_template, get_templates_path, get_date, get_time
from mastawrap.base.utils.journal import Journal
from mastawrap.base.templates.templater import Templater
from mastawrap.constructor.workCamp.farmer.farmer import Farmer
from mastawrap.constructor.workCamp.farms.farmState import FarmState
from mastawrap.logger.logger import Logger, logger


class Manager:
    """
    Cette classe sert à gérer les ajouts et retraits de workers dans
    l'application. Elle gère les abonnements au différentes fermes
    nécessaires au constructeur pour enfiler les jobs de traduction.

    :param Context le contexte de l'application (ne devrait contenir que
                   les informations nécessaires au Manager !!!)
    """

    instance = None
    farmField = None

    def __init__(self, context):
        if not self.instance:
            self.instance = self._Manager(context)
            self.instance.journal.createEntry("treating_ticket")
            self.instance.journal.log("treating_ticket")
        else:
            ContextManager.replace_context(self.instance, context)

    """
    Méthodes publiques
    """

    def createFarms(self, names):
        if not self.farmField:
            self._initializeField(self.instance.context)
        self._createFarm(names)

    def assignTask(self, task):
        if task["inLanguage"] in self.instance.context["inLanguages"]:
            self._verifyTemplateAvailability([
                task["inLanguage"],
                task["outLanguage"]
            ])
            self._assertCompatibility(task)
            self._createTreatingTicket(task)
        else:
            print("impossible d'effectuer le traitement")

    def close(self):
        self.instance.exit()

    """
    Méthodes privées
    """

    # INITIALIZATION ET CREATION
    def _initializeField(self, context):
        self.farmField = self.__FarmField(context)

    def _createFarm(self, names):
        for name in names:
            print(name)
            self.farmField.addFarmer(name)

    # DEMANDE DE TRAITEMENT

    def _createTreatingTicket(self, task):
        self.instance.journal.logEvent("treating_ticket", task)
        # TODO add a listener to the treating ticket list to automate conversion

    def _verifyTemplateAvailability(self, languages = []):
        for language in languages:
            try:
                open(get_templates_path() + "\\languages\\" + language + ".json")
            except IOError:
                print("Langage " + language + " absent.")

    def _assertCompatibility(self, task):
        self.farmField.verifyCombinaison(task)

    """
    Classe interne du manager, s'occupe de créer l'instance et de
    tenir les sections du journal d'opérations à jour.
    """
    class _Manager(Resource):
        def __init__(self, context):
            super().__init__(context)
            # Init du journal
            self._journal = Journal(context, "MANAGER_JOURNAL")
            self._journal.logEvent = lambda key, value: self._logEvent(self._journal, key, value)
            self._journal.logEvent("logs", "ManagerCreation : " + str(id(self)))
            self._journal.log("logs")

        def _getJournal(cls):
            return cls._journal

        def _logEvent(self, journal, key, val):
            if key is "log":
                val = "[" + get_date + "]:" + get_time + " - :" + val
            journal.createEntry(key)
            h = journal.handbook[key]["content"]
            h.append(val)
            # TODO: MAKE BEAUTIFUL AND WORK

        def exit(self):
            self.journal.record()

        journal = property(_getJournal)

    class __FarmField(Resource):
        """
        Le manager du camp de travail peut créer des champs de fermes
        qui contiendront des fermiers. Chaque fermier se verra attitré
        à une ferme selon son langage de programmation.

        """
        # TODO: Décrire le lien entre les langages entrants et sortant et la façon d'optimiser le traitement
        # TODO: Ajouter une gestion de scaling des fermes selon les demandes de traduction et les farmers
        # TODO: Gérer les ressources disponibles selon les informations du contexte

        field = dict()

        def __init__(self, context):
            super().__init__(context)

        def addFarmer(self, name):
            # TODO: Ajouter le fermier dans le dictionaire field
            # TODO: Créer l'entité de traitement (à raffiner)
            # L'entité peut être un process, on pourrait vouloir rouler le farmer sur une machine différente, à voir
            farmer = self._spawnFarms(FarmState.EMPTY)
            farmer["name"] = name
            print(farmer)

        def verifyCombinaison(self, task):
            farms = self._parseField({
                "inLanguage": task["inLanguage"]
            })
            # TODO : Implémenter la logique de vérification de fermiers
            # Doit-on directement refuser la demande de traitement si les fermes ne sont
            # pas directement disponibles ? Doit-on envoyer un avis d'attente puis une
            # notification ? (Système d'abonnement)

        @logger("__FarmField")
        def _spawnFarms(self, state, lang=None):
            context = ContextManager.prepContextFor("farmer", self.context, {
                "lang": lang,
                "state": state
            })
            self.field[len(self.field)] = Farmer(context)
            return self.field[len(self.field)]
            # TODO: Méthode bidon, ajouter la mécanique de spawn de ferme réelle

        def _parseField(self, parseOptions = dict()):
            a = []
            for key in parseOptions:
                for farm in self.field.values():
                    a = self._keep_if_candidate(a, farm, key, parseOptions[key])
            return a

        def _keep_if_candidate(self, a, farm, key, val):
            if farm[key] == val:
                return a.append(farm)
            else:
                return a



