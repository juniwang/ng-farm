__author__ = 'Junbo Wang'
__version__ = '1.0'

from flask import Flask
from flask_restful import Api
from log import log

# flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a_te$t_K3y!!!'


class FarmApi(Api):
    """Customize Api to give a chance to handle exceptions in framework level
    We can raise HTTPException and it's inheritances directly in components, they will be caught here. Now we have two
    ways to response with error:
        - return bad_request("some message")
        - raise Bad_Request("some message")
    You can decide to use either way ,they are of the same.
    """

    def handle_error(self, e):
        log.error(e)
        return self.make_response(e.message, 500)

# flask restful
api = FarmApi(app)

from . import views
