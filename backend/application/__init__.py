from flask import Flask
from flask_cors import CORS
from .controller.letterController import letter
from .controller.userController import user
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
CORS(app)
app.secret_key = 'cky0935'

app.register_blueprint(letter)
app.register_blueprint(user)

