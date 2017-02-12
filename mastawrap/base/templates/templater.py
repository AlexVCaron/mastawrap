from enum import Enum, unique
from mastawrap.base.utils import utils
import os


class Templater:


    def _get_path(self):
        return __file__

    """
    SECTION ENUMS
    Les enums contenus dans la section suivante contiennent les liens vers les différents templates nécessaires
    au bon déroulement de l'application. Le templater a pour l'instant un fonctionnement un peu complexe et marche
    en accordance avec des enums internes qui contiennent des clés dont les valeurs sont des chemins en string
    vers les templates

        CHEMINS : les chemins s'écrivent à partir du répertoire templates et sans le .json
            - exemple de chemin : farmers.base
    """

    @unique
    class FarmStates(Enum):
        EMPTY = "farmers.base"
        SPAWNING = "farmers.spawning"
        IDLE = None
        RUNNING = "farmers.running"
        ERROR = "farmers.error"

    @unique
    class Worker(Enum):
        EMPTY = "worker.base"

    # TODO: Déplacer les enums de liens vers un fichier différent, voir créer un package pour le templater
    # Dans le cas où le package est créé, ajouter à get_path un load on
    # the fly des enums au besoin d'un path
    @classmethod
    def get_path(cls, link):
        """
            retourne le path vers un template dans l'application. Pour
            ajouter des liens, on crée un enum avec les liens vers les
            templates respectifs comme valeur des clés
        :param link: un lien définit dans un Enum (ex : FarmStates.EMPTY)
        :return:
        """
        str = (utils.get_templates_path() + "\\" + eval("cls." + link.value).value).replace(".", "\\")
        return  str + ".json"