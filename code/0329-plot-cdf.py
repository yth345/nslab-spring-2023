import csv
import os, glob
from matplotlib import pyplot as plt
from datetime import datetime, timedelta


def main():
    log_data = []
    read_log(log_data, './log.out')

    mk_path = f'./plot/ip-coverage'
    if not os.path.isdir(mk_path):
        os.mkdir(mk_path)

    for c_info in log_data:
        channels = []
        print(c_info)
        ttl_hn_cnt = sort_data(c_info, channels)
        # plot_each_round(c_info, channels, ttl_hn_cnt)
        plot_agg_round(c_info, channels, ttl_hn_cnt)


def read_log(log_data, path):
    with open(path, 'r') as f:
        lines = [line.split('\t') for line in f.readlines()]
        for l in lines:
            if 'connecting' in l[1]:
                vpn_host = l[1].split()[0].split('.')[0]
                start_t = l[0]
            if 'checkCountry' in l[1]:
                country = l[1].split()[1]
                ip = l[1].split()[2].lstrip('(').rstrip(')')
            if 'disconnected' in l[1]:
                end_t = l[0]
                log_data.append([start_t, end_t, country, vpn_host, ip])


def sort_data(c_info, channels):
    round_start_t = datetime.fromisoformat(c_info[0][:-1])
    round_end_t = datetime.fromisoformat(c_info[1][:-1])
    country = c_info[3] + c_info[2]
    vpn_ip = c_info[4]

    all_hn_set = set()
    edgs_fn = glob.glob(os.path.join(f'./mapped/', '*.tsv'))
    for path in edgs_fn:
        ft = path.split('/')[-1][:-5]
        pb_time = datetime.fromisoformat(ft[:-4].replace('.', ':') + ft[-4:])
        if pb_time < round_start_t - timedelta(minutes=15) or pb_time > round_end_t:
            continue
        
        channel_in_round = []
        with open(path, 'r') as f:
            f.readline()
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                user_login = row[1]
                node = row[2]
                user_ip = row[3]
                if user_ip != vpn_ip:  # only count the correct ones
                    continue
                all_hn_set.add(node)
                channel_in_round.append([user_login, node, int(row[5])])  # user_login, node, viewer_cnt

        channel_in_round.sort(key=lambda x: int(x[2]), reverse=True)  # sort based on viewer count
        channels.append(channel_in_round)

    return len(all_hn_set)


def plot_each_round(c_info, channels, ttl_hn_cnt):
    country = c_info[3] + c_info[2]

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
    plt.savefig(f'./plot/ip-coverage/{country}.png', dpi=300)
    print(f"{country} finished")


def plot_agg_round(c_info, channels, ttl_hn_cnt):
    country = c_info[3] + c_info[2]
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
    ax.plot([x for x in range(max_channel_cnt)], coverage)
    ax.set_ylim([-0.1, 1.1])
    ax.grid()
    plt.title(f'{country}')
    plt.xlabel('# of Channels in Each Round (Sorted by Viewer Count)')
    plt.ylabel('IP Coverage Ratio')
    # plt.show()
    plt.savefig(f'./plot/ip-coverage/agg-{country}.png', dpi=300)
    print(f"{country} aggregate finished")


if __name__ == '__main__':
    main()


