from flask import Flask

# init app
app = Flask(__name__)

# handle configuration
app.config.update(
    DEBUG=False,
)

# import custom python files
from app import views
from app import jinja_functions
