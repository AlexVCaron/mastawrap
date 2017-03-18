def require_template(templateField):
    def createEvent(eventCreationFunction):
        def templateToEvent(*args):
            args = list(args)
            klass = args.pop(0)
            id = args.pop(0)
            template = EventTemplateManager.requireTemplate(templateField, id)
            event = template.fillAndFetch(*tuple(args))
            eventCreationFunction(klass, id, event)
        return templateToEvent
    return createEvent


class EventTemplateManager(object):
    templates = dict()

    def __getattr__(self, item):
        try:
            return self.templates[item]
        except KeyError:
            print("Register a template field first ! {} Inexistant".format(item))

    def __init__(self):
        self.templates["translation"] = {}

    @classmethod
    def registerTranslationEventTemplate(cls, template):
        return cls.registerEventTemplate("translation", template)

    @classmethod
    def registerEventTemplate(cls, section, template):
        if section in cls.templates:
            id = len(cls.templates[section])
            cls.templates[section][id] = template
        else:
            id = 0
            cls.templates[section] = {id : template}
        return id

    @classmethod
    def requireTemplate(cls, section, templateId):
        return cls.templates[section][templateId] if section in cls.templates and templateId in cls.templates[section] else None