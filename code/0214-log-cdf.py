import csv
import os, glob
from matplotlib import pyplot as plt
from tqdm import tqdm


def main():
    #city_lst_1 = ['Amsterdam']
    city_lst_1 = ['Amsterdam', 'Copenhagen', 'Frankfurt', 'London', 'Madrid', 'Marseille', 'Milan', 'Oslo', 'Paris']
    city_lst_2 = ['Berlin', 'Helsinki', 'Prague', 'Stockholm', 'Vienna', 'Warsaw']

    for city in city_lst_1:
        plot(f'k5081_100k_25Hz_eu15_48R_1D/k5081_{city}')
        print(f'{city} done')

    for city in city_lst_2:
        plot(f'k5082_100k_25Hz_eu6_48R_1D/k5082_{city}')
        print(f'{city} done')


def plot(c):
    CHANNEL_CNT = 100000
    edgs_fn = glob.glob(os.path.join(f'./{c}/edgs-w-info-sorted/', '*.csv'))
    
    top_channel_ip = []
    ttl_ip_set = set()
    for fn in edgs_fn:
        with open(fn, 'r') as f:
            f.readline()
            reader = list(csv.reader(f))

            tmp_code_list = []
            for row in reader:
                hostname = row[2]
                if error_hn(hostname):
                    continue
                hn_seg = row[2].split('.')
                server_code = hn_seg[0][-6:] + '.' + hn_seg[1]
                ttl_ip_set.add(server_code)
                tmp_code_list.append(server_code)
                
        while len(tmp_code_list) < CHANNEL_CNT:
            tmp_code_list.append('END')
        top_channel_ip.append(tmp_code_list)


    ip_set = set()
    num_of_ip = []

    for i in tqdm(range(CHANNEL_CNT)):
        for ip_list in top_channel_ip:
            if ip_list[i] != 'END':
                ip_set.add(ip_list[i])
        num_of_ip.append(len(ip_set))

    ttl_ip_cnt = len(ttl_ip_set)
    ip_coverage = [n / ttl_ip_cnt for n in num_of_ip]
    city_name = c.split('/')[1][6:]

    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.plot([i for i in range(1, CHANNEL_CNT + 1)], ip_coverage)
    # ax.plot([x for x in range(0, 101)], ip_coverage)
    ax.grid()
    plt.title(f'{city_name}')
    plt.xlabel('Number of Channels, Sorted by Viewer Count')
    plt.ylabel('IP Coverage Ratio')
    plt.ylim(-0.1, 1.1)
    plt.xscale('log')
    # plt.show()
    plt.savefig(f'./{c}/{city_name}.png', dpi=300)


def error_hn(hn):
    error_msg = ['Request failed', 'socket hang up', 'timeout of', 'disconnected', 'EAI_AGAIN', 'ETIMEDOUT',\
                 'maxContentLength', 'Cannot read properties', 'ECONNRESET']
    for err in error_msg:
        if err in hn:
            return True
    return False
    

if __name__ == '__main__':
    main()
