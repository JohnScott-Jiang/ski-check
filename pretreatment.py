import os
import sys

import cv2

import yolo


# 把目录下的所有视频保存为图像
def save_video_to_image(video_dir):
    output_dir = os.path.join(video_dir, 'output')
    os.makedirs(output_dir, exist_ok=True) # 新建输出目录
    for videoname in os.listdir(video_dir): # 遍历每个视频
        if not os.path.isfile(os.path.join(video_dir, videoname)): # 如果不是文件，则跳过
            continue
        print(videoname)
        name, ext = os.path.splitext(videoname)
        vid = cv2.VideoCapture(os.path.join(video_dir, videoname))
        if vid is None:
            continue
        for i in range(100000000):
            ret, frame = vid.read()
            if frame is None:
                break
            cv2.imwrite(os.path.join(output_dir, '%s_%04d.jpg' %(name, i)), frame)

if __name__ == '__main__' :
    source_datapath=sys.argv[1]
    save_video_to_image(source_datapath)
    datapath=os.path.join(source_datapath,'output')
    yolo.run(source=datapath)
