from yolo import YOLO
from yolo import detect_video

if __name__ == '__main__':
    video_path = 0
    output_path = './output.avi'
    # detect_video(YOLO(), video_path, output_path)
    detect_video(YOLO(),video_path)