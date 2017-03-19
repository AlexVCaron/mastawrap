class MetaEventManager(type):
    events = {}

    def __getitem__(self, item):
        return self.events[item] if item in self else self.events[item]

    def __setitem__(self, key, value):
        self.events[key] = value if key in self else self.events[key]

    def __contains__(self, item):
        self.createSection(item) if item not in self.events else None
        return True

    def getSection(self, section):
        return self[section]

    def createSection(self, section):
        self.events[section] = list()
