from app import app
from flask import request

def menu_active(path):
	if path in request.path:
		return 'class="active"'
	else:
		return ''

app.jinja_env.globals.update(menu_active=menu_active)
