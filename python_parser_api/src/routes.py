from src import api
from src.resources.test import Test
from src.resources.character import Сharacter
#
# Declarations of app routes in type of rest web-architecture
#

# routes
api.add_resource(Test, '/test', strict_slashes=False)
api.add_resource(Сharacter, '/character/<name>', strict_slashes=False)