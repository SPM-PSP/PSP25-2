import cv2
import time

class Capture:
    """用于捕获本地摄像头视频流的类"""
    
    def __init__(self, camera_id=0):
        """
        初始化视频捕获对象
        
        Parameters:
        -----------
        camera_id : int, optional
            摄像头ID，默认为0（通常是第一个摄像头）
        """
        self.camera_id = camera_id
        self.cap = None
        self.connected = False
    
    def connect(self):
        """连接到摄像头"""
        try:
            self.cap = cv2.VideoCapture(self.camera_id)
            if not self.cap.isOpened():
                print(f"无法打开摄像头 ID: {self.camera_id}")
                return False
            
            self.connected = True
            return True
        except Exception as e:
            print(f"连接摄像头时发生错误: {e}")
            return False
    
    def read_frame(self):
        """
        读取当前帧
        
        Returns:
        --------
        tuple: (success, frame)
            success: 布尔值，表示是否成功读取帧
            frame: 如果成功，返回捕获的帧；否则为None
        """
        if not self.connected:
            print("摄像头未连接，请先调用connect()")
            return False, None
        
        return self.cap.read()
    
    def release(self):
        """释放视频捕获资源"""
        if self.cap is not None:
            self.cap.release()
            self.connected = False
    
    def get_fps(self):
        """获取摄像头的帧率"""
        if not self.connected:
            return 0
        return self.cap.get(cv2.CAP_PROP_FPS)
    
    def get_resolution(self):
        """获取视频分辨率"""
        if not self.connected:
            return (0, 0)
        width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        return (width, height)
    
    def set_resolution(self, width, height):
        """设置视频分辨率"""
        if not self.connected:
            return False
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        return True


# 示例用法
if __name__ == "__main__":
    capture = Capture(camera_id=0)  # 使用默认摄像头
    
    if capture.connect():
        print(f"摄像头已连接。分辨率: {capture.get_resolution()}, FPS: {capture.get_fps()}")
        
        try:
            while True:
                ret, frame = capture.read_frame()
                if ret:
                    # 显示捕获的帧
                    cv2.imshow('local', frame)
                    
                    # 按下'q'键退出
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    print("无法读取帧")
                    break
                    
        finally:
            capture.release()
            cv2.destroyAllWindows()
            print("已释放资源")
    else:
        print("无法连接到摄像头")
