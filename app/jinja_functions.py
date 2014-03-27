from app import app
from flask import request
from datetime import datetime, timedelta

def menu_active(path):
	if path in request.path:
		return 'class="active"'
	else:
		return ''

def now():
	return datetime.now() + timedelta(hours=1) # adjust ireland timezone to brussels timezone

app.jinja_env.globals.update(menu_active=menu_active)
app.jinja_env.globals.update(now=now)
