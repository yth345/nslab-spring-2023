import csv
import os, glob
from matplotlib import pyplot as plt

channels = []

def main():
    path_list = ['k1001_100k_nl1033_24R', 'k1002_100k_se597_18R', 'k1003_100k_pl220_22R', 'k1004_100k_at120_24R', 'k5110_100k_EU13_24R']
    for path in path_list:
        sort_data(path)
        print(f'finish sorting {path}')
    plot()


def sort_data(ds_path):
    edgs_fn = glob.glob(os.path.join(f'./{ds_path}/mapped/', '*.tsv'))
    for path in edgs_fn:
        channel_in_round = []
        with open(path, 'r') as f:
            f.readline()
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                # user_login = row[1]
                node = row[2]
                viewer_cnt = int(row[5])
                channel_in_round.append([node, viewer_cnt])

        channel_in_round.sort(key=lambda x: int(x[1]), reverse=True)  # sort based on viewer count
        channels.append(channel_in_round)


def plot():
    max_channel_cnt = 0
    for pb_round in channels:
        if len(pb_round) > max_channel_cnt:
            max_channel_cnt = len(pb_round)
    
    hn_set = set()
    unique_hn_cnt = []
    for i in range(max_channel_cnt):
        for pb_round in channels:
            if i >= len(pb_round):
                continue
            hostname = pb_round[i][0]
            hn_set.add(hostname)
        unique_hn_cnt.append(len(hn_set))

    ttl_hn_cnt = len(hn_set)
    coverage = [cnt / ttl_hn_cnt for cnt in unique_hn_cnt]

    found = [False, False, False, False, False, False]
    ratio = [0.6, 0.7, 0.8, 0.9, 0.95, 0.99]
    for i in range(len(coverage)):
        for j in range(len(ratio)):
            if not found[j] and coverage[i] > ratio[j]:
                print(f'coverage ratio > {ratio[j]} at {i+1}-th channel')
                found[j] = True

    print(f'coverage ratio at 1000 channels: {coverage[999]}')
    print(f'coverage ratio at 2000 channels: {coverage[1999]}')
    print(f'coverage ratio at 3000 channels: {coverage[2999]}')
    print(f'coverage ratio at 4000 channels: {coverage[3999]}')
    print(f'coverage ratio at 5000 channels: {coverage[4999]}')
    print(f'coverage ratio at 10000 channels: {coverage[9999]}')
    print(f'coverage ratio at 40000 channels: {coverage[39999]}')

    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.plot([x for x in range(max_channel_cnt)], coverage)
    ax.grid()
    plt.title(f'EU 13 Aggregated IP Coverage Ratio')
    plt.xlabel('# of Channels (Sorted by Viewer Count)')
    plt.ylabel('IP Coverage Ratio')
    # plt.xscale('log')
    plt.savefig(f'./EU13-ttl-ip-coverage.png', dpi=300)
    # plt.savefig(f'./log-EU13-ttl-ip-coverage.png', dpi=300)


if __name__ == '__main__':
    main()
