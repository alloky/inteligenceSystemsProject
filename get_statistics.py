import json
import numpy as np

from matplotlib import pyplot as plt


def get_length_list(indexfile):
    content = json.load(open(indexfile))
    length_list = []

    for entry in content:
        duration = entry['end_time'] - entry['start_time']
        length_list.append(duration)
    return length_list

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
    plt.hist(length_list)
    plt.show()


if __name__ == '__main__':
    print_stat('MSASL_train.json')
    print_stat('MSASL_test.json')
    print_stat('MSASL_val.json')

