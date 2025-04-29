from app import create_app
from app.services import camera_service
from app.services.model import model_service
import threading
import os  
app = create_app()
threading.Thread(target=model_service.run_inference_service, daemon=True).start()
threading.Thread(target=camera_service.start_camera_service, daemon=True).start()
if __name__ == '__main__':
    app.run(debug=True)