from flask import request, render_template, url_for, redirect
from app import app

# Main pages
@app.route('/')
def index():
    return render_template('home.html', title="Home")

@app.route('/search')
def search():
    return render_template('search.html', title="Search", heading="Search")

@app.route('/we-are')
def we_are():
    return render_template('we-are.html', title="+ We Are", heading="+ We Are")

@app.route('/media')
def media():
    return render_template('media.html', title="Media", heading="Media")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")

@app.route('/your-campaign')
def campaign():
    return render_template('your-campaign.html', title="Your Campaign", heading="Your Campaign")

@app.route('/research')
def research():
    return render_template('research.html', title="We're in Touch", heading="We're in Touch")

# side bar menu
@app.route('/audio-visual')
def audio_visual():
    return render_template('audio-visual.html', title="Audio Visual", heading="Audio Visual")

@app.route('/videos')
def videos():
    return render_template('videos.html', title="Videos", heading="Videos")

@app.route('/social-media')
def social_media():
    return render_template('social-media.html', title="Social Media", heading="Social Media")

@app.route('/events')
def events():
    return render_template('events.html', title="Events & Organisation", heading="Events & Organisation")

@app.route('/editorial')
def editorial():
    return render_template('editorial.html', title="Editorial & New Content", heading="Editorial & New Content")
