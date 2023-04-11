import csv
import os, glob
from matplotlib import pyplot as plt


def main():
    country_list = ['k1001_100k_nl1033_24R', 'k1002_100k_se597_18R', 'k1003_100k_pl220_22R', 'k1004_100k_at120_24R']
    for c in country_list:
        channels = []
        print(f"{c} start")
        ttl_hn_cnt = sort_data(c, channels)
        # plot_each_round(c, channels, ttl_hn_cnt)
        plot_agg_round(c, channels, ttl_hn_cnt)


def sort_data(c_path, channels):
    country = c_path.split('_')[2]
    all_hn_set = set()
    edgs_fn = glob.glob(os.path.join(f'./{c_path}/mapped/', '*.tsv'))
    for path in edgs_fn:
        channel_in_round = []
        with open(path, 'r') as f:
            f.readline()
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                user_login = row[1]
                node = row[2]
                all_hn_set.add(node)
                channel_in_round.append([user_login, node, int(row[5])])  # user_login, node, viewer_cnt

        channel_in_round.sort(key=lambda x: int(x[2]), reverse=True)  # sort based on viewer count
        channels.append(channel_in_round)
    return len(all_hn_set)


def plot_each_round(c_path, channels, ttl_hn_cnt):
    country = c_path.split('_')[2]

    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    for i in range(len(channels)):
        hn_set = set()
        coverage = []
        for j in range(len(channels[i])):
            hostname = channels[i][j][1]
            hn_set.add(hostname)
            coverage.append(len(hn_set) / ttl_hn_cnt)
        
        # plot 
        ax.plot([x for x in range(len(channels[i]))], coverage)

    ax.grid()
    plt.title(f'{country}')
    plt.xlabel('# of Channels (Sorted by Viewer Count)')
    plt.ylabel('IP Coverage Ratio')
    # plt.show()
    plt.savefig(f'./{c_path}/plot/{country}-ip-coverage.png', dpi=300)
    print(f"{country} finished")


def plot_agg_round(c_path, channels, ttl_hn_cnt):
    country = c_path.split('_')[2]
    max_channel_cnt = 0
    for i in range(len(channels)):
        if len(channels[i]) > max_channel_cnt:
            max_channel_cnt = len(channels[i])

    hn_set = set()
    coverage = []
    for i in range(max_channel_cnt):
        for j in range(len(channels)):
            if len(channels[j]) - 1 < i:
                continue
            hostname = channels[j][i][1]
            hn_set.add(hostname)
        coverage.append(len(hn_set) / ttl_hn_cnt)

    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.set_ylim([-0.1, 1.1])
    ax.plot([x for x in range(max_channel_cnt)], coverage)
    ax.grid()
    plt.title(f'{country}')
    plt.xlabel('# of Channels in Each Round (Sorted by Viewer Count)')
    plt.ylabel('IP Coverage Ratio')
    # plt.show()
    plt.savefig(f'./{c_path}/plot/agg-{country}-ip-coverage.png', dpi=300)
    print(f"{country} aggregate finished")


if __name__ == '__main__':
    main()
