import json
import numpy as np

from collections import defaultdict


def get_length_list(indexfile):
    content = json.load(open(indexfile))
    intervals = defaultdict(list)

    for entry in content:
        intervals[entry['url']].append((entry['start_time'], entry['end_time']))
    gaps = []
    for key in intervals.keys():
        if not len(intervals[key]):
            pass
        intervals[key] = sorted(intervals[key])
        if intervals[key][0][0] > 0.0:
            gaps.append(intervals[key][0][0])

        for i in range(1, len(intervals[key])):
            if intervals[key][i][0] < intervals[key][i-1][1]:
                #print(intervals[key])
                continue
            if 1.5 <= intervals[key][i][0] - intervals[key][i-1][1] <= 4.5:
                gaps.append(intervals[key][i][0] - intervals[key][i-1][1])

    print("total", len(content))
    print("gaps len", len(gaps))
    return gaps

def print_stat(indexfile):
    length_list = get_length_list(indexfile)
    print('=' * 50)
    print(indexfile)
    print('mean', np.mean(length_list))
    print('median', np.median(length_list))
    print('min', np.min(length_list))
    print('max', np.max(length_list))
    print('quantile 0.2', np.percentile(length_list, q=20))
    print('quantile 0.8', np.percentile(length_list, q=80))

if __name__ == '__main__':
    print_stat('MSASL_train.json')
    print_stat('MSASL_test.json')
    print_stat('MSASL_val.json')


