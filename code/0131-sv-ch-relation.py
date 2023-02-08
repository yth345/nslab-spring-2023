# analyze relation between servers (hoastname) and channels

import csv
import os, glob
from matplotlib import pyplot as plt
from datetime import datetime
import math

def main():
    # city_lst_1 = ['Frankfurt']
    city_lst_1 = ['Amsterdam', 'Copenhagen', 'Frankfurt', 'London', 'Madrid', 'Marseille', 'Milan', 'Oslo', 'Paris']
    city_lst_2 = ['Berlin', 'Helsinki', 'Prague', 'Stockholm', 'Vienna', 'Warsaw']

    for city in city_lst_1:
        # process(f'k5081_{city}')
        plot(f'k5081_{city}')
    for city in city_lst_2:
        # process(f'k5082_{city}')
        plot(f'k5082_{city}')

def process(c):
    hn_dict = dict()
    p_time_list = []
    file_list = glob.glob(os.path.join(f'code/2023-EU15/{c}/server', '*.csv'))
    for fpath in sorted(file_list):
        p_time = fpath.split('/')[-1][:-9]
        p_time_list.append(p_time)
        with open(fpath, 'r') as f:
            f.readline()
            reader = csv.reader(f)
            for row in reader:
                hostname = row[0]
                unique_ch_cnt = int(row[1])
                max_viewer_cnt = int(row[2])
                hn_seg = hostname.split('.')
                hn = hn_seg[0][-6:] + '.' + hn_seg[1]
                if hn not in hn_dict:
                    hn_dict[hn] = [[p_time, unique_ch_cnt, max_viewer_cnt]]
                else:
                    hn_dict[hn].append([p_time, unique_ch_cnt, max_viewer_cnt])

    ch_cnt_list = []
    viewer_cnt_list = []
    for key, value in hn_dict.items():
        subnet_w_code = key[7:] + '.' + key[:6]
        ch_cnt_row = [subnet_w_code]
        viewer_cnt_row = [subnet_w_code]
        for pt in p_time_list:
            find_match = False
            for v in value:
                if pt == v[0]:
                    ch_cnt_row.append(v[1])
                    viewer_cnt_row.append(v[2])
                    find_match = True
                    break
            if not find_match:
                ch_cnt_row.append(0)
                viewer_cnt_row.append(0)
        ch_cnt_list.append(ch_cnt_row)
        viewer_cnt_list.append(viewer_cnt_row)

    # sort by subnet and code
    ch_cnt_sorted = sorted(ch_cnt_list, key=lambda x: x[0])
    viewer_cnt_sorted = sorted(viewer_cnt_list, key=lambda x: x[0])

    w_path = f'code/2023-EU15/{c}/unique-ch-cnt-sorted.csv'
    with open(w_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['server_code'] + p_time_list)
        for row in ch_cnt_sorted:
            writer.writerow(row)
    
    w_path = f'code/2023-EU15/{c}/max-viewer-cnt-sorted.csv'
    with open(w_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['server_code'] + p_time_list)
        for row in viewer_cnt_sorted:
            writer.writerow(row)


def plot(c, sorted=True):
    # unique channel count
    if sorted:
        r_path = f'code/2023-EU15/{c}/unique-ch-cnt-sorted.csv'
        w_path = f'code/2023-EU15/images/unique-channel-cnt-sorted/{c[6:]}.png'
    else:
        r_path = f'code/2023-EU15/{c}/unique-ch-cnt.csv'
        w_path = f'code/2023-EU15/images/unique-channel-cnt/{c[6:]}.png'

    grid = []
    with open(r_path, 'r') as f:
        tmp = f.readline().split(',')
        reader = csv.reader(f)
        print(f'{c[6:]} time count: {len(tmp) - 1}')
        for row in reader:
            new_row = [int(element) for element in row[1:]]
            grid.append(new_row)
    
    fig, ax = plt.subplots(1, 1, figsize=(4,8))
    ax.set_ylim([422, 0])
    plt.title(f'{c[6:]}')
    plt.xlabel('probing round')
    plt.ylabel('hostname label', )
    
    pos = plt.imshow(grid)
    fig.colorbar(pos, shrink=0.5)
    plt.savefig(w_path, dpi=300)
    

    # ln max viewer count
    if sorted:
        r_path = f'code/2023-EU15/{c}/max-viewer-cnt-sorted.csv'
        w_path = f'code/2023-EU15/images/max-viewer-cnt-sorted/{c[6:]}.png'
    else:
        r_path = f'code/2023-EU15/{c}/max-viewer-cnt.csv'
        w_path = f'code/2023-EU15/images/max-viewer-cnt/{c[6:]}.png'

    grid = []
    with open(r_path, 'r') as f:
        tmp = f.readline().split(',')
        reader = csv.reader(f)
        print(f'{c[6:]} time count: {len(tmp) - 1}')
        for row in reader:
            new_row = [int(element) for element in row[1:]]
            for i in range(len(new_row)):
                if new_row[i] > 0:
                    new_row[i] = math.log(new_row[i])
            grid.append(new_row)
    
    fig, ax = plt.subplots(1, 1, figsize=(4,8))
    ax.set_ylim([422, 0])
    plt.title(f'{c[6:]}')
    plt.xlabel('probing round')
    plt.ylabel('hostname label', )
    
    pos = plt.imshow(grid)
    fig.colorbar(pos, shrink=0.5)
    plt.savefig(w_path, dpi=300)

if __name__ == '__main__':
    main()