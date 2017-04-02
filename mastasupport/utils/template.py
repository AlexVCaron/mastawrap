import json
import os

from mastawrap.base import templates


def load_from_template(template):
    print(template)
    d = json.load(template)
    return d


def get_templates_path():
    return os.path.dirname(os.path.realpath(templates.__file__))
