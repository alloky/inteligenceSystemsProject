import json
import os
import re

def process_directory(target_txt, ds_path, json_file):
        contents = json.load(open(json_file))
        valid_ids = os.listdir(ds_path)
        if 'flow' in valid_ids:
            valid_ids.remove('flow')

        with open(target_txt, "w") as f:
            n_records = 0
            for content in contents:
                video_id = re.findall(r"/watch\?v=(.+)", content['url'])[0]
                if content['label'] >= 100:
                    continue
                if video_id not in valid_ids:
                    continue

                f.write('{} {} {} {}\n'.format(video_id, content['start'], content['end'], content['label']))
                n_records += 1
                                                                                                            
            print(target_txt.split('_')[0] + "records prepared: ", n_records)


if __name__ == '__main__':
    process_directory('train_records_new.txt', '/home/mlepekhin/train_frames_big', '../MSASL_train.json')
    process_directory('test_records_new.txt', '/home/mlepekhin/test_frames_big', '../MSASL_test.json')
    process_directory('val_records_new.txt', '/home/mlepekhin/val_frames_big', '../MSASL_val.json')

