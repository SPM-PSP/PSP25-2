from flask import Flask
from app.routes.video import video_bp
from flask_cors import CORS 
def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.register_blueprint(video_bp)
    return app