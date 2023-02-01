'''
datasets
k5072: big-5 countries, one day
k5080: EU-15 cities, one hour
k5081, k5082: EU-15 cities, one day
'''

import csv
import os, fnmatch
import json
from datetime import datetime


def main():
    city_lst_1 = ['Amsterdam', 'Copenhagen', 'Frankfurt', 'London', 'Madrid', 'Marseille', 'Milan', 'Oslo', 'Paris']
    # city_lst_1 = ['Amsterdam']
    city_lst_2 = ['Berlin', 'Helsinki', 'Prague', 'Stockholm', 'Vienna', 'Warsaw']

    for city in city_lst_1:
        map_info(f'k5081_100k_25Hz_eu15_48R_1D/k5081_{city}')
        get_server_view(f'k5081_100k_25Hz_eu15_48R_1D/k5081_{city}')
        print(f'{city} done')

    for city in city_lst_2:
        map_info(f'k5082_100k_25Hz_eu6_48R_1D/k5082_{city}')
        get_server_view(f'k5082_100k_25Hz_eu6_48R_1D/k5082_{city}')
        print(f'{city} done')


def map_info(c):
    # probe_file_list = sorted(os.listdir(f'./{c}/edgs/'))
    # stream_info_file_list = sorted(os.listdir(f'./{c}/strm/'))
    probe_file_list = sorted(fnmatch.filter(os.listdir(f'./{c}/edgs/'), '*.tsv'))
    stream_info_file_list = sorted(fnmatch.filter(os.listdir(f'./{c}/strm/'), '*.txt'))

    info_dict = dict()
    for fn in stream_info_file_list:
        info_t = datetime.fromisoformat(fn[:-14].replace('.', ':'))
        path = f'./{c}/strm/{fn}'
        with open(path, 'r') as f:
            for row in f:
                raw = json.loads(row)
                for data in raw['data']:
                    user_login = data['user_login']
                    language = data['language']
                    viewer_cnt = int(data['viewer_count'])

                    if user_login not in info_dict:
                        info_dict[user_login] = [[info_t, language, viewer_cnt]]
                    else:
                        info_dict[user_login].append([info_t, language, viewer_cnt])

    ttl_probe_cnt = 0
    for fn in probe_file_list:
        probe_t = datetime.fromisoformat(fn[:-9].replace('.', ':'))
        r_path = f'./{c}/edgs/{fn}'
        with open(r_path, 'r') as rf:
            reader = csv.reader(rf, delimiter='\t')
            w_path = f'./{c}/edgs-w-info/{fn[:-4]}.csv'
            with open(w_path, 'w', newline='') as wf:
                writer = csv.writer(wf)
                writer.writerow(['user_login', 'probe_t', 'hostname', 'language', 'viewer_cnt'])
                for row in reader:
                    # compare time and find the closest info before probe
                    ttl_probe_cnt += 1
                    ptime = row[0]
                    hostname = row[1]
                    user_login = row[2]
                    entry_cnt = len(info_dict[user_login])
                    if entry_cnt == 1:
                        language = info_dict[user_login][0][1]
                        viewer_cnt = info_dict[user_login][0][2]

                    for i in range(entry_cnt - 1):
                        curr_info = info_dict[user_login][i]
                        next_info = info_dict[user_login][i + 1]
                        next_t = next_info[0]
                        if probe_t > next_t:
                            # last entry
                            if (i + 1) == (entry_cnt - 1):
                                language = next_info[1]
                                viewer_cnt = next_info[2]
                            continue
                        else:
                            language = curr_info[1]
                            viewer_cnt = curr_info[2]
                            break
                    writer.writerow([user_login, ptime, hostname, language, viewer_cnt])
        print(f'{c}, {fn[:-4]} done')
    print(f'total probe cnt: {ttl_probe_cnt}')


def get_server_view(c):
    error_msg = ['Request failed', 'socket hang up', 'timeout of', 'disconnected', 'EAI_AGAIN', 'ETIMEDOUT', 'maxContentLength', 'Cannot read properties']
    file_list = sorted(fnmatch.filter(os.listdir(f'./{c}/edgs-w-info/'), '*.csv'))
    for fn in file_list:
        r_path = f'./{c}/edgs-w-info/{fn}'
        hn_dict = dict()
        with open(r_path, 'r') as f:
            reader = csv.reader(f)
            f.readline()
            for row in reader:
                user_login = row[0]
                hostname = row[2]
                language = row[3]
                viewer_cnt = int(row[4])
                # ignore errors
                skip = False
                for err in error_msg:
                    if err in hostname:
                        skip = True
                if skip:
                    continue

                if hostname not in hn_dict:
                    hn_dict[hostname] = [set([user_login]), set([language]), viewer_cnt]
                else:
                    hn_dict[hostname][0].add(user_login)
                    hn_dict[hostname][1].add(language)
                    if viewer_cnt > hn_dict[hostname][2]:
                        hn_dict[hostname][2] = viewer_cnt
        
        w_path = f'./{c}/server/{fn}'
        with open(w_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['hostname', 'unique_channel_cnt', 'max_viewer_cnt', 'language'])
            for key, value in hn_dict.items():
                writer.writerow([key, len(value[0]), value[2], value[1]])
        print(f'{c}, {fn[:-4]} done')


if __name__ == '__main__':
    main()
