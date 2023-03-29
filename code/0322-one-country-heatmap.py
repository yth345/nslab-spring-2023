import csv
import os, glob
from matplotlib import pyplot as plt
import math


def main():
    country_list = ['k1001_100k_nl1033_24R', 'k1002_100k_se597_18R', 'k1003_100k_pl220_22R', 'k1004_100k_at120_24R']
    for c in country_list:
        process_data(c)
        plot_concise(c)


def process_data(c_path):
    country = c_path.split('_')[2]
    hn_dict = dict()
    pb_time_list = []
    sv_list = sorted(glob.glob(os.path.join(f'./{c_path}/server', '*.tsv')))
    for path in sv_list:
        pb_time = path.split('/')[-1].lstrip(country)[1:-5]
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

    mk_path = f'./{c_path}/plot'
    if not os.path.isdir(mk_path):
        os.mkdir(mk_path)

    w_path = f'./{c_path}/plot/{country}-unique-ch-cnt.csv'
    with open(w_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['server_code'] + pb_time_list)
        for row in ch_cnt_sorted:
            writer.writerow(row)
    
    w_path = f'./{c_path}/plot/{country}-max-viewer-cnt.csv'
    with open(w_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['server_code'] + pb_time_list)
        for row in viewer_cnt_sorted:
            writer.writerow(row)


def plot_concise(c_path):
    country = c_path.split('_')[2]

    # unique channel count
    r_path = f'./{c_path}/plot/{country}-unique-ch-cnt.csv'
    w_path = f'./{c_path}/plot/{country}-concise.png'

    grid = []
    y_label = []
    c_dict = dict()
    with open(r_path, 'r') as f:
        pb_rounds = [t[5:16] for t in f.readline().split(',')[1:]]
        reader = csv.reader(f)
        # print(f'{country} time count: {len(pb_rounds)}')
        for row in reader:
            cluster = row[0].split('.')[0]
            new_row = [int(element) for element in row[1:]]
            if cluster in c_dict:
                c_dict[cluster] = [[sum(i) for i in zip(c_dict[cluster][0], new_row)], c_dict[cluster][1] + 1]
            else:
                c_dict[cluster] = [new_row, 1]
        for key, value in c_dict.items():
            y_label.append(f'{key} ({value[1]})')
            grid.append(value[0])

    fig, ax = plt.subplots(1, 1)
    # ax.set_ylim([339, 0])
    # fig.autofmt_xdate()
    ax.set_xticks([i for i in range(len(pb_rounds))], pb_rounds, rotation=90)
    ax.set_yticks([i for i in range(len(y_label))], y_label)

    plt.title(f'{country}-unique-ch-cnt')
    plt.xlabel('probing round')
    plt.ylabel('cluster')
    plt.tight_layout()
    
    pos = plt.imshow(grid)
    fig.colorbar(pos, shrink=0.3)
    plt.savefig(w_path, dpi=300)


if __name__ == '__main__':
    main()