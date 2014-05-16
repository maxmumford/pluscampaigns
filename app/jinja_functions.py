from app import app
from flask import request
import random

def menu_active(path):
	if path in request.path:
		return 'class="active"'
	else:
		return ''

def random_background_image():
	images = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png', '10.png', '11.png']
	return images[random.randint(0, len(images)-1)]

app.jinja_env.globals.update(menu_active=menu_active)
app.jinja_env.globals.update(random_background_image=random_background_image)
