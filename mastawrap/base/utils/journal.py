from mastawrap.base.resource import Resource


class Journal(Resource):

    def __init__(self, context, name):
        super().__init__(context)
        self.handbook = dict()
        self.name = name

    def createEntry(self, key):
        if not key in self.handbook:
            self.handbook[key] =  {
                "isLoggable": False,
                "content": []
            }

    def log(self, key):
        if key in self.handbook:
            self.handbook[key]["isLoggable"] = True

    def logEvent(self, entry, event):
        self.createEntrie(entry)
        self.handbook[entry].append(event)

    def record(self):
        try:
            f = open(self.context["log_dir"] + self.name + ".log", "w")
            for log in self.handbook:
                if self.handbook[log]["isLoggable"]:
                    f.write("------------------------------\n")
                    f.write("LOG_NAME : " + log + "\n")
                    for event in self.handbook[log]["content"]:
                        f.write("--- " + event + "\n")
        except IOError as e:
            print(e)
            print("Failed to log")

    def __del__(self):
        self.record()



