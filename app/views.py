from flask import request, render_template, url_for, redirect, flash, send_from_directory
from app import app

from datetime import datetime
import uuid
import os
import threading
import Image

""" Check a file's extension against image whitelist """
def get_file_extension(file_name):
    file_name = file_name.lower()
    return '.' in file_name and file_name.rsplit('.', 1)[1]

# Main pages
@app.route('/')
def index():
    return render_template('home.html', title="Video", publish=datetime(2014, 03, 28, 12, 00, 00))

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

# Happify
@app.route('/happify', methods=['GET', 'POST'])
def happify():
    if request.method == 'GET':
        return render_template('happify.html', title="Happify My Photo!", heading=False)

    else: # request is post
        uploadedFile = request.files['file']
        extension = get_file_extension(uploadedFile.filename)

        if extension and extension in {'png', 'jpg', 'jpeg', 'gif'}:

            try:
                # setup filename and prepare save directory
                file_name = '%s.%s' % (str(uuid.uuid4()), extension)
                if(not os.path.isdir(app.config['UPLOAD_FOLDER'])):
                    os.makedirs(app.config['UPLOAD_FOLDER'])

                # Open uploaded image and watermark, then make thumbnail from watermark to have the appropriate size for big and small overlays
                image = Image.open(uploadedFile)

                watermark = Image.open('app/static/images/happify/happify-watermark.png')
                watermark.thumbnail(image.size, Image.ANTIALIAS)

                # calculate the position of the watermark
                watermark_width, watermark_height = watermark.size
                image_width, image_height = image.size
                paste_position = (image_width / 2 - (watermark_width / 2), image_height / 2 - (watermark_height / 2))

                # do actual watermarking and save the image
                image.paste(watermark, paste_position, watermark)
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))

                # redirect to /happify with image url in parameter
                return render_template('happify.html', title="Happify My Photo!", heading=False, image=url_for('uploads', file_name=file_name))
            except Exception as e:
                print e
                return render_template('happify.html', title="Happify My Photo!", heading=False)

        else: # bad file extension
            flash("Please check the file type of your image. We only accept png, jpg, jpeg and gif.")
            return render_template('happify.html', title="Happify My Photo!", heading=False)

@app.route('/uploads/<file_name>')
def uploads(file_name):
    return send_from_directory(app.config['UPLOAD_FOLDER'], file_name)

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
