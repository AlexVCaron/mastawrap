from random import Random

from mastawrap.base.resource import Resource
from mastawrap.base.templates.templater import Templater
from mastawrap.base.utils.utils import load_from_template
from mastawrap.constructor.workCamp.farmer.worker.worker import Worker
from mastawrap.constructor.workCamp.farmer.worker.workerState import WorkerState


class Farmer(Resource):


    _config = dict()


    """
    Le contexte de la ferme doir contenir les champs suivants
    --- "inLanguage" : le champ du langage de la ferme
    --- "start_state" : l'étât dans lequel partir le fermier dans
                        l'éventualité d'un redémarrage
    """
    def __init__(self, context):
        super().__init__(context)
        self.st = Templater.FarmStates(context["start_state"])
        self.load_farm()
        if "nb_worker" in self._config["__init__"] and self._config["__init__"]["nb_worker"] > 0:
            self._spawn_workers_langs(self._config["__init__"]["nb_worker"],
                                self._config["__init__"]["languages"],
                                self._config["__init__"]["base_conf"])
        else:
            self.workerDict = load_from_template(WorkerState.EMPTY)


    def load_farm(self):
        self._constructFromTemplate()


    def _get_inLanguage(self):
        return self.context["inLanguage"]

    inLanguage = property(_get_inLanguage)

    def _get_state(self):
        return self.st

    def _set_state(self, state):
        self.st = state

    state = property(_get_state, _set_state)

    def _get_workers(self):
        out = dict()
        for worker in self.workerDict:
            out[worker["id"]] = {
                "lang": worker["language"],
                "mode": worker["mode"],
                "used": worker["is_used"]
            }
        return out

    workers = property(_get_workers)

    def _constructFromTemplate(self):
        self._config = load_from_template(open(Templater.get_path(self.st)))
        print("FARM LOADED" + self._config[len(self._config) - 1]["name"])
        return self._config[len(self._config) - 1]

    def _spawn_workers_langs(self, qty, langs = [], conf = {}):
        spl = qty / len(langs)
        for lang in langs:
            self._spawn_workers(spl, lang, conf)
        if divmod(qty, len(langs)) > 0:
            self._spawn_workers(divmod(qty, len(langs)), langs[0], conf)

    def _spawn_workers(self, qty, lang, conf):
        self._check_language_presence(lang)
        for i in range(1,qty):
            wk = self._add_worker(lang)
            self._conf_worker(wk, lang, conf)

    def _check_language_presence(self, lang):
        if not lang in self.workerDict:
            self.workerDict[lang] = dict()

    def _add_worker(self, lang):
        tag = self._create_worker_tag()
        self.workerDict[lang][tag] = Worker(self.context)
        return tag

    def _create_worker_tag(self):
        return "worker_" + self._get_name() + "_" + Random()

    def _get_name(self):
        return self.context["name"]

    def _conf_worker(self, lang, worker, conf):
        wk = self.workerDict[lang][worker]
        wk.configurate(conf)