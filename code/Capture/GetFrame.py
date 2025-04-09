from Capture import Capture
import cv2
import requests
import numpy as np
import json
import base64
import time

def get_image_from_api(api_url, headers=None, params=None):
    """
    从API获取图片
    
    Args:
        api_url: API地址
        headers: 请求头信息，默认为None
        params: 请求参数，默认为None
        
    Returns:
        OpenCV格式的图像，如果获取失败则返回None
    """
    if headers is None:
        headers = {}
    
    try:
        response = requests.get(api_url, headers=headers, params=params, timeout=2)
        response.raise_for_status()  # 如果请求失败则抛出异常
        
        # 判断返回的是JSON还是二进制图像数据
        content_type = response.headers.get('Content-Type', '')
        
        if 'application/json' in content_type:
            # 如果是JSON，尝试从中提取Base64编码的图像
            data = response.json()
            if 'image' in data:
                # Base64编码的图像
                img_data = base64.b64decode(data['image'])
                nparr = np.frombuffer(img_data, np.uint8)
                img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                return img
        else:
            # 否则尝试直接作为图像数据处理
            nparr = np.frombuffer(response.content, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            return img
            
    except Exception as e:
        print(f"从API获取图片时出错: {str(e)}")
        return None

def stream_images_from_api(api_url, fps=30):
    """
    持续从API获取图像流并显示
    
    Args:
        api_url: API地址
        fps: 每秒获取图像的频率
    """
    print(f"正在从 {api_url} 获取图像流")
    print("按 'q' 键退出")
    
    frame_interval = 1.0 / fps  # 计算帧间隔时间
    
    while True:
        start_time = time.time()
        time.sleep(0.1)  # 确保每次循环都有时间间隔
        image = get_image_from_api(api_url)
        
        if image is not None:
            cv2.imshow("Image Stream", image)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("获取图像失败，重试中...")
            time.sleep(1)  # 获取失败时等待一秒再重试
            
        # 计算需要等待的时间以维持所需FPS
        elapsed_time = time.time() - start_time
        sleep_time = max(0, frame_interval - elapsed_time)
        if sleep_time > 0:
            time.sleep(sleep_time)
    
    cv2.destroyAllWindows()
    print("图像流接收已停止")

if __name__ == "__main__":
    api_url = "http://127.0.0.1:5000"  # 替换为实际的API地址
    
    # 持续获取图像流
    stream_images_from_api(api_url, fps=30)