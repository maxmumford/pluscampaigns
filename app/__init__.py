from flask import Flask

# init app
app = Flask(__name__)

# handle configuration
app.config.update(
    DEBUG=True,
    SECRET_KEY='\xeeJ\x97\xe4\x9f\x96\xe6\xc3\xe7:\xca\xc9L}F\xb3\xe6\x84\xfa\xaf\x8d\x14\x83\xa4'
)

# import views
from app import views
