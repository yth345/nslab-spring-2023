import csv
import os, glob
from matplotlib import pyplot as plt
import math


def main():
    log_data = []
    read_log(log_data, './log.out')
    country_list = [dt[2] for dt in log_data]
    for country in country_list:
        process_data(country)
        plot(country)


def read_log(log_data, path):
    with open(path, 'r') as f:
        lines = [line.split('\t') for line in f.readlines()]
        for l in lines:
            if 'connecting' in l[1]:
                vpn_host = l[1].split()[0]
                start_t = l[0]
            if 'checkCountry' in l[1]:
                country = l[1].split()[1]
                ip = l[1].split()[2].lstrip('(').rstrip(')')
            if 'disconnected' in l[1]:
                end_t = l[0]
                log_data.append([start_t, end_t, country, vpn_host, ip])


def process_data(country):
    hn_dict = dict()
    pb_time_list = []
    sv_list = sorted(glob.glob(os.path.join(f'server', '*.tsv')))
    for path in sv_list:
        country_code = path.split('/')[-1][:2]
        if country_code != country:
            continue

        pb_time = path.split('/')[-1][3:-5]
        pb_time_list.append(pb_time)
        with open(path, 'r') as f:
            f.readline()
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                hn_seg = row[0].split('-')[-1].split('.')
                hn = hn_seg[1] + '.' + hn_seg[0]
                unique_ch_cnt = int(row[1])
                max_viewer_cnt = int(row[2])
                if hn not in hn_dict:
                    hn_dict[hn] = [[pb_time, unique_ch_cnt, max_viewer_cnt]]
                else:
                    hn_dict[hn].append([pb_time, unique_ch_cnt, max_viewer_cnt])

    ch_cnt_list = []
    viewer_cnt_list = []
    for key, value in hn_dict.items():
        ch_cnt_row = [key]
        viewer_cnt_row = [key]
        for pt in pb_time_list:
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

    mk_path = f'./plot'
    if not os.path.isdir(mk_path):
        os.mkdir(mk_path)

    w_path = f'plot/{country}-unique-ch-cnt.csv'
    with open(w_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['server_code'] + pb_time_list)
        for row in ch_cnt_sorted:
            writer.writerow(row)
    
    w_path = f'plot/{country}-max-viewer-cnt.csv'
    with open(w_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['server_code'] + pb_time_list)
        for row in viewer_cnt_sorted:
            writer.writerow(row)


def plot(country):
    # unique channel count
    r_path = f'plot/{country}-unique-ch-cnt.csv'
    w_path = f'plot/{country}-unique-ch-cnt.png'

    grid = []
    y_label = []
    with open(r_path, 'r') as f:
        pb_rounds = [t[5:16] for t in f.readline().split(',')[1:]]
        reader = csv.reader(f)
        print(f'{country} time count: {len(pb_rounds)}')
        for row in reader:
            y_label.append(row[0])
            new_row = [int(element) for element in row[1:]]
            grid.append(new_row)
    
    fig, ax = plt.subplots(1, 1, figsize=(6,10))
    ax.set_ylim([339, 0])
    # fig.autofmt_xdate()
    # ax.set_xticks([i for i in range(len(pb_rounds))], pb_rounds, rotation=90, fontsize=6)
    # ax.set_yticks([i for i in range(len(y_label))], y_label, fontsize=6)

    plt.title(f'{country}-unique-ch-cnt')
    plt.xlabel('probing round')
    plt.ylabel('hostname label')
    plt.tight_layout()
    
    pos = plt.imshow(grid)
    fig.colorbar(pos, shrink=0.3)
    plt.savefig(w_path, dpi=300)
    
    '''
    # ln max viewer count
    r_path = f'plot/{country}-max-viewer-cnt.csv'
    w_path = f'plot/{country}-max-viewer-cnt.png'

    grid = []
    with open(r_path, 'r') as f:
        tmp = f.readline().split(',')
        reader = csv.reader(f)
        print(f'{country} time count: {len(tmp) - 1}')
        for row in reader:
            new_row = [int(element) for element in row[1:]]
            for i in range(len(new_row)):
                if new_row[i] > 0:
                    new_row[i] = math.log(new_row[i])
            grid.append(new_row)
    
    fig, ax = plt.subplots(1, 1, figsize=(4,8))
    ax.set_ylim([422, 0])
    plt.title(f'{country}')
    plt.xlabel('probing round')
    plt.ylabel('hostname label')
    
    pos = plt.imshow(grid)
    fig.colorbar(pos, shrink=0.5)
    plt.savefig(w_path, dpi=300)
    '''

if __name__ == '__main__':
    main()