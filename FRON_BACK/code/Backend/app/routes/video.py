from flask import Blueprint, send_file, abort
import os

video_bp = Blueprint('video', __name__)

PICTURE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'data', 'picture', 'latest.jpg')
PICTURE_PATH = os.path.abspath(PICTURE_PATH)

@video_bp.route('/video/display')
def display_picture():
    if os.path.exists(PICTURE_PATH):
        return send_file(PICTURE_PATH, mimetype='image/jpeg')
    else:
        abort(404, description="Picture not found")