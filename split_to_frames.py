import cv2
import json
import os
import shutil

from multiprocessing import Pool
from os import listdir
from tqdm import tqdm

def process_video(video_arg):
    source_video, target_dir, fps = video_arg
    vidcap = cv2.VideoCapture(source_video)

    def getFrame(sec):
        vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        hasFrames,image = vidcap.read()
        if hasFrames:
          image = cv2.resize(image, (224, 224))
          cv2.imwrite(target_dir + '/' + str(count) + '.jpg', image)     # save frame as JPEG file
        return hasFrames

    sec = 0
    frameRate = fps / 60
    count=1
    success = getFrame(sec)
    while success:
        count += 1
        sec += frameRate
        sec = round(sec, 2)
        success = getFrame(sec)

def process_directory(source_dir, target_dir, json_file):
    contents = json.load(open(json_file))
    id_to_fps = {}
    for content in contents:
        video_id = content['url'][len('https://www.youtube.com/watch?v='):]
        id_to_fps[video_id] = content['fps']

    shutil.rmtree(target_dir, ignore_errors=True)
    os.makedirs(target_dir, mode=0o777)

    video_list = []

    for source_video in tqdm(listdir(source_dir)):
        #print("source_video", source_video)
        video_id = source_video[:source_video.find('.')]
        os.makedirs(target_dir + '/' + video_id, mode=0o777)
        #print("VIDEO_ID", video_id)
        video_list.append([
            source_dir + '/' + source_video,
            target_dir + '/' + video_id,
            id_to_fps[video_id] if video_id in id_to_fps else 30.0
        ])
    print(len(video_list))
    with Pool(processes=10) as p:
        p.map(process_video, video_list)


if __name__ == '__main__':
    process_directory('train', 'train_frames', 'MSASL_train.json')
    process_directory('test', 'test_frames', 'MSASL_test.json')
    process_directory('val', 'val_frames', 'MSASL_val.json')

