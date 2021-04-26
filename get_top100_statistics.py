import cv2
import json
import numpy as np

from os.path import isfile
from os.path import join as pathjoin
from tqdm import tqdm


def print_top_stat(indexfile):
    print()
    print(indexfile)
    print('-' * 50)
    content = json.load(open(indexfile))
    succ_num = np.zeros(100).astype(int)
    fail_num = np.zeros(100).astype(int)
    total_succ_num, total_fail_num = 0, 0

    total_frames = 0
    top_frames = 0
    for entry in tqdm(content):
        filename = entry['url'][entry['url'].find('?v=')+3:] + '.mp4'
        filename = pathjoin(indexfile[6:-5], filename)

        if isfile(filename):
            if entry['label'] < 100:
                succ_num[entry['label']] += 1
            total_succ_num += entry['label'] >= 100

            v = cv2.VideoCapture(filename)
            cur_frames = v.get(cv2.CAP_PROP_FRAME_COUNT)
            total_frames += cur_frames
            top_frames += (entry['label'] >= 100) * cur_frames
        else:
            if entry['label'] < 100:
                fail_num[entry['label']] += 1
            total_fail_num += entry['label'] >= 100
    print("total success_num:", total_succ_num, "total failure num:", total_fail_num)
    print("min success_num:", np.min(succ_num))
    print("mean success num:", np.mean(succ_num))
    print("median success num:", np.median(succ_num))
    print("max success num:", np.max(succ_num))
    print("min share", np.min(succ_num / (fail_num + succ_num)))
    print("all succ counts:", list(succ_num))
    print("all shares:", list([round(x, 2) for x in succ_num / (succ_num + fail_num)]))
    print("total frames:", total_frames, "top frames:", top_frames, "frames share:", top_frames / total_frames)

if __name__ == '__main__':
    print_top_stat('MSASL_train.json')
    print_top_stat('MSASL_test.json')
    print_top_stat('MSASL_val.json')

