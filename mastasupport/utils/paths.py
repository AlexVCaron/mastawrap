import os

import mastawrap


def get_path(file):
    os.path.dirname(os.path.realpath(file))


def get_logs_path():
    return get_base_path() + "\\logs\\"


def get_base_path():
    return os.path.dirname(os.path.realpath(mastawrap.__file__))