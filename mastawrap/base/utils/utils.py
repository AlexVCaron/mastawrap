import json.decoder
from mastawrap.base import templates
import mastawrap
import os
import datetime


def load_from_template(template):
    print(template)
    d = json.load(template)
    return d

def get_path(file):
    os.path.dirname(os.path.realpath(file))

def get_templates_path():
    return os.path.dirname(os.path.realpath(templates.__file__))

def get_logs_path():
    return get_base_path() + "\\logs\\"

def get_base_path():
    return os.path.dirname(os.path.realpath(mastawrap.__file__))

def get_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S.f")