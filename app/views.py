from flask import render_template, flash, url_for
from app import app

@app.route('/')
def index():
    return render_template('home.html', title="Home")

@app.route('/campaign')
def campaign():
    return render_template('campaign.html', title="Your Campaign", heading="Your Campaign", image_source="4")

@app.route('/about')
def about():
    return render_template('about.html', title="Young Voters", heading="Vote In May", image_source="1")

@app.route('/take-action')
def share():
    return render_template('take-action.html', title="Take Action", heading="Take Action", image_source="3")

@app.route('/media')
def media():
    return render_template('media.html', title="Media", heading="Media Resources", image_source="2")
