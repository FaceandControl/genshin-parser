from src import api
from src.resources.test import Test
#
# Declarations of app routes in type of rest web-architecture
#

# routes
api.add_resource(Test, '/test', strict_slashes=False)