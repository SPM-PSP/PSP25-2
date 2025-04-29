import cv2
import os
import time
import threading
PICTURE_INTERVAL = 0.1  # 秒
VIDEO_FRAME_COUNT = 30
VIDEO_INTERVAL = 0.1    # 秒
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, '..', 'data')
PICTURE_DIR = os.path.join(DATA_DIR, 'picture')
VIDEO_DIR = os.path.join(DATA_DIR, 'video')

# 自动创建目录
os.makedirs(PICTURE_DIR, exist_ok=True)
os.makedirs(VIDEO_DIR, exist_ok=True)

PICTURE_PATH = os.path.join(PICTURE_DIR, 'latest.jpg')

def update_picture(camera):
    while True:
        ret, frame = camera.read()
        if ret:
            cv2.imwrite(PICTURE_PATH, frame)
        time.sleep(PICTURE_INTERVAL)

def update_video_frames(camera):
    idx = 0
    frames = []
    while True:
        frames.clear()
        for i in range(VIDEO_FRAME_COUNT):
            ret, frame = camera.read()
            if ret:
                frame_path = os.path.join(VIDEO_DIR, f'frame_{i+1:02d}.jpg')
                cv2.imwrite(frame_path, frame)
                frames.append(frame_path)
            time.sleep(VIDEO_INTERVAL)
        # 3秒后自动覆盖前面的帧

def start_camera_service():
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("无法打开摄像头")
        return

    t1 = threading.Thread(target=update_picture, args=(camera,), daemon=True)
    t2 = threading.Thread(target=update_video_frames, args=(camera,), daemon=True)
    t1.start()
    t2.start()

    print("摄像头服务已启动，按 Ctrl+C 退出。")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        camera.release()
        print("已退出。")

