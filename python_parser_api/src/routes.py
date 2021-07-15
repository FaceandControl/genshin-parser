from src import api
from src.resources.main import Main
from src.resources.character import Сharacter
from src.resources.characters import Сharacters
#
# Declarations of app routes in type of rest web-architecture
#

# routes
api.add_resource(Main, '/', strict_slashes=False)
api.add_resource(Сharacter, '/<ln>/character/<name>', strict_slashes=False)
api.add_resource(Сharacters, '/<ln>/characters', strict_slashes=False)