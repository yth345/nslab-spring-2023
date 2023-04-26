import csv
import os, glob
from matplotlib import pyplot as plt
from datetime import datetime, timedelta

country_ips = []
vpn_name = []

def main():
    all_hn_set = set()
    log_data = []
    read_log(log_data, './k5110_100k_EU13_24R/log.out')
    for c_info in log_data:
        print(c_info)
        correct = get_country_ip_set(all_hn_set, c_info, 'k5110_100k_EU13_24R')
        if correct:
            vpn_name.append(c_info[3])

    one_country_list = ['k1001_100k_nl1033_24R', 'k1002_100k_se597_18R', 'k1003_100k_pl220_22R', 'k1004_100k_at120_24R']
    for ds in one_country_list:
        correct = get_country_ip_set(all_hn_set, c_info, ds, False)
        vpn_name.append(ds.split('_')[2])
        print(f'{ds} done, {len(all_hn_set)}')

    
    # overlapping IP amount among countries
    grid = []
    for i in range(len(country_ips)):
        row = []
        for j in range(len(country_ips)):
            row.append(100 * len(country_ips[i].intersection(country_ips[j])) / len(country_ips[i]))
        grid.append(row)

    fig, ax = plt.subplots(1, 1)
    ax.set_xticks([i for i in range(len(country_ips))], vpn_name, rotation=45, ha="right", rotation_mode="anchor")
    ax.set_yticks([i for i in range(len(country_ips))], vpn_name)

    plt.title(f'Overlapping % of IPs from diff VPN')
    plt.ylabel('with respect to')
    plt.tight_layout()
    
    plt.imshow(grid)
    for i in range(len(country_ips)):
        for j in range(len(country_ips)):
            ax.text(j, i, "{:.0f}".format(grid[i][j]), ha="center", va="center", color="w", fontsize=9)

    plt.savefig('./overlap-ratio.png', dpi=300)

    
    # find country set cover
    '''
    remain_ip_cnt = len(all_hn_set)
    selected = []
    while (remain_ip_cnt > 0):
        max_cover_cnt = 0
        idx = 0
        for i in range(len(country_ips)):
            cover_server_cnt = len(all_hn_set.intersection(country_ips[i]))
            if cover_server_cnt > max_cover_cnt:
                max_cover_cnt = cover_server_cnt
                idx = i

        selected.append(vpn_name[idx])
        all_hn_set = all_hn_set.difference(country_ips[idx])
        remain_ip_cnt = len(all_hn_set)

        for i in range(len(country_ips)):
            country_ips[i] = country_ips[i].difference(country_ips[idx])
        print(f'select {vpn_name[idx]}, new discovered server count: {max_cover_cnt}')
    print(f'selected vpn:\n{selected}')
    '''
    

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


def get_country_ip_set(all_hn_set, c_info, ds_path, multi_country=True):
    err_host = ['nl979', 'at130', 'se596', 'fi200']
    if multi_country:
        vpn_host = c_info[3]
        if vpn_host in err_host:
            return False
        round_start_t = datetime.fromisoformat(c_info[0][:-1])
        round_end_t = datetime.fromisoformat(c_info[1][:-1])
        vpn_ip = c_info[4]

    edgs_fn = glob.glob(os.path.join(f'./{ds_path}/mapped/', '*.tsv'))
    ip_set = set()
    for path in edgs_fn:
        if multi_country:
            ft = path.split('/')[-1][:-5]
            pb_time = datetime.fromisoformat(ft[:-4].replace('.', ':') + ft[-4:])
            if pb_time < round_start_t - timedelta(minutes=15) or pb_time > round_end_t:
                continue
        with open(path, 'r') as f:
            f.readline()
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                node = row[2]
                user_ip = row[3]
                if multi_country and user_ip != vpn_ip:  # only count the correct ones
                    continue
                ip_set.add(node)
                all_hn_set.add(node)

    country_ips.append(ip_set)
    return True
    

if __name__ == '__main__':
    main()