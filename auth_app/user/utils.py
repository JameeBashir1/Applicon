from flask import current_app
from flask_login import current_user
from secrets import token_hex
from PIL import Image
import os


def save_picture(picture):
    old_filename = current_user.profile_picture
    if old_filename != 'default.png':
        if os.path.exists(os.path.join(current_app.root_path, 'static', 'profile_pictures', old_filename)):
            old_path = os.path.join(current_app.root_path, 'static', 'profile_pictures', old_filename)
            os.remove(old_path)

    random_hex = token_hex(8)
    _, ext = os.path.splitext(picture.filename)
    filename = random_hex + ext
    path = os.path.join(current_app.root_path, 'static', 'profile_pictures', filename)

    size = (215, 215)
    i = Image.open(picture)
    i.thumbnail(size)
    i.save(path)

    return filename
























