import os
import secrets
from PIL import Image
from flask import url_for, current_app



def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    # to get extension of the file
    _, f_ext = os.path.splitext(form_picture.filename)
    #form_picture = data from the field what users submits. If it's a file, then it will have .filename attribute
    picture_fn = random_hex + f_ext
    #full name where this variable will be saved that python knows where he will be saving it.
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)


    output_size = (125, 125)
    #Now Using Pillow library modules
    i = Image.open(form_picture)#Opens and identifies the given image file.
    i.thumbnail(output_size)#Make this image into a thumbnail. This method modifies the image to contain a thumbnail version of itself, no larger than the given size.
    i.save(picture_path) # before was form_picture.save(picture_path) but now its new picture = i which is resized (what is created above) we save only resized pics.

    return picture_fn#picture file name
