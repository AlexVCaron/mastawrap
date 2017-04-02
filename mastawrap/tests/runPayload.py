from mastawrap.constructor.workCamp.manager import Manager

from mastasupport.utils.paths import get_logs_path

context = {
    "a": "A", "b": "B",
    "log_dir": get_logs_path()
}
names = ["c++", "csharp", "python", "ruby"]
man = Manager(context)
man.createFarms(names)
man.close()