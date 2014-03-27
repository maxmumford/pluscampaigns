from flask import render_template, url_for, redirect
from app import app

# Main pages
@app.route('/')
def index():
    return render_template('home.html', title="Home")

@app.route('/making-of')
def making_of():
    return render_template('making-of.html', title="The Making Of", heading="The Making Of Happy Voting", image_source="3")

@app.route('/campaign')
def campaign():
    return render_template('campaign.html', title="Your Campaign", heading="Your Campaign", image_source="6")

@app.route('/about')
def about():
    return render_template('about.html', title="Young Voters", heading="Vote In May", image_source="7")

@app.route('/take-action')
def share():
    return render_template('take-action.html', title="Take Action", heading=False, image_source="2")

@app.route('/media')
def media():
    return render_template('media.html', title="Media", heading="Media Resources", image_source="1")

@app.route('/blog')
def blog():
    return render_template('blog.html', title="Blog", heading=False)

# Other
@app.route('/cookies')
def cookies():
    return render_template('cookies.html', title="Cookies", heading="Cookie Information")
    
@app.route('/donation-thanks')
def donation_thanks():
	return render_template('donation-thanks.html', title="Donation", heading="Thanks for your donation!", image_source="4")

@app.route('/donation-cancel')
def donation_cancel():
	return redirect(url_for('share'))
