from mastawrap.base.resource import Resource

class Worker(Resource):

    def __init__(self, context):
        super().__init__(context)

    def configurate(self, conf):
        self.conf = conf
        # TODO: BIDON POUR TEST SEULEMENT, SERT A CONFIGURER MAIS EST SEULEMENT OVERRIDEN