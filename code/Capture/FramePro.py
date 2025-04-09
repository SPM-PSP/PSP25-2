from Capture import Capture
import cv2
import requests
import numpy as np
import json
import base64
import time
from flask import Flask, Response
import threading
import signal
import sys

# 创建 Flask 应用
app = Flask(__name__)

# 全局变量用于存储最新的帧
latest_frame = None
frame_lock = threading.Lock()
server_running = True

# Flask 路由，用于提供最新的图片帧
@app.route('/')
def serve_frame():
    global latest_frame
    with frame_lock:
        if latest_frame is None:
            return Response("No frame available", status=404)
        # 返回 JPEG 格式的图像
        return Response(latest_frame, mimetype='image/jpeg')

# 在一个单独的线程中运行 Flask 服务器
def run_flask_server():
    app.run(host='127.0.0.1', port=5000, debug=False, threaded=True, use_reloader=False)

def FramePro(capture, fps=30, width=640, height=480):
    global latest_frame, server_running
    
    if not capture.connected:
        print("摄像头未连接，请先调用connect()")
        return
    
    # 启动 Flask 服务器的线程
    flask_thread = threading.Thread(target=run_flask_server)
    flask_thread.daemon = True
    flask_thread.start()
    
    print("图像传输服务已启动，监听端口：127.0.0.1:5000")
    print("按 'q' 键退出")
    try:
        while server_running:
            success, frame = capture.read_frame()
            if not success:
                print("无法读取帧")
                break
            # 调整帧大小
            frame = cv2.resize(frame, (width, height))
            # 将帧编码为 JPEG 格式
            _, jpeg_frame = cv2.imencode('.jpg', frame)
            with frame_lock:
                latest_frame = jpeg_frame.tobytes()

    except KeyboardInterrupt:
        print("用户中断，正在关闭...")
    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        server_running = False
        capture.release()
        cv2.destroyAllWindows()
        print("图像传输服务已关闭")

if __name__ == "__main__":
    capture = Capture(camera_id=0)  # 使用默认摄像头
    if capture.connect():
        print(f"摄像头已连接。分辨率: {capture.get_resolution()}, FPS: {capture.get_fps()}")
        FramePro(capture, fps=30, width=640, height=480)
    else:
        print("无法连接到摄像头")
        capture.release()
