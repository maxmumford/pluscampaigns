from app import app
from flask import request
import random

def menu_active(path):
	if path in request.path:
		return 'class="active"'
	else:
		return ''

def random_background_image():
	images = ['1.jpg', '2.jpg', '3.png', '4.JPG', '5.jpg', '6.jpg', '7.jpg', '8.png', '9.jpg', '10.jpg', '11.jpg']
	return images[random.randint(0, len(images)-1)]

app.jinja_env.globals.update(menu_active=menu_active)
app.jinja_env.globals.update(random_background_image=random_background_image)
