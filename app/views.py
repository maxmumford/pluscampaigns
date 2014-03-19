from flask import render_template, flash, url_for
from app import app

@app.route('/')
def index():
    return render_template('home.html', title="Home")

@app.route('/about')
def about():
    return render_template('about.html', title="Young Voters")

@app.route('/media')
def media():
    return render_template('media.html', title="Media")

@app.route('/share')
def share():
    return render_template('share.html', title="Share")

@app.route('/donate')
def donate():
    return render_template('donate.html', title="Donate")
