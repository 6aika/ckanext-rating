import ckan.plugins as p

from ckanext.rating.blueprint import rating as rating_blueprint
import ckanext.rating.cli as cli

class MixinPlugin(p.SingletonPlugin):

    p.implements(p.IBlueprint)
    p.implements(p.IClick)

    def get_blueprint(self):
        return [rating_blueprint]

    def get_commands(self):
        return cli.get_commands()