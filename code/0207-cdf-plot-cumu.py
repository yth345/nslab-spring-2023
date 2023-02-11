import csv, itertools
import os, glob
from matplotlib import pyplot as plt
from tqdm import tqdm

def main():
    # make file name list
    path_list = []
    city_lst_1 = ['Amsterdam', 'Copenhagen', 'Frankfurt', 'London', 'Madrid', 'Marseille', 'Milan', 'Oslo', 'Paris']
    city_lst_2 = ['Berlin', 'Helsinki', 'Prague', 'Stockholm', 'Vienna', 'Warsaw']
    
    for city in city_lst_1:
        path_list.append(f'k5081_100k_25Hz_eu15_48R_1D/k5081_{city}')
    for city in city_lst_2:
        path_list.append(f'k5082_100k_25Hz_eu6_48R_1D/k5082_{city}')

    plot(path_list)


def plot(path_list):
    start = 0
    ip_set = set()
    num_of_ip = []
    # percentage of total probed channel count
    # for i in (x * 0.5 for x in range(0, 201)):
    for i in tqdm(range(0, 101)):

        for p in path_list:  # each city
            edgs_fn = glob.glob(os.path.join(f'./{p}/edgs-w-info-sorted/', '*.csv'))

            row_cnt_list = []
            for fn in edgs_fn:
                with open(fn, 'r') as f:
                    f.readline()
                    reader = csv.reader(f)
                    row_cnt = sum(1 for row in reader)
                    row_cnt_list.append(row_cnt)

            idx = 0
            for fn in edgs_fn:
                with open(fn, 'r') as f:
                    f.readline()
                    reader = csv.reader(f)
                    # sort rows in csv file by viewer count
                    sorted_data = sorted(reader, key=lambda x: int(x[4]), reverse=True)

                    row_cnt = row_cnt_list[idx]
                    end = int(i * 0.01 * row_cnt)
                    idx += 1

                    for row in itertools.islice(sorted_data, start, end):
                        hostname = row[2]
                        if error_hn(hostname):
                            continue
                        hn_seg = hostname.split('.')
                        server_code = hn_seg[0][-6:] + '.' + hn_seg[1]
                        ip_set.add(server_code)

        num_of_ip.append(len(ip_set))
        start = end

    ttl_ip_cnt = len(ip_set)
    ip_coverage = [n / ttl_ip_cnt for n in num_of_ip]

    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.plot([x for x in range(0, 101)], ip_coverage)
    ax.grid()
    plt.title(f'EU 15 Cities')
    plt.xlabel('Top Channel Percentage')
    plt.ylabel('IP Coverage Ratio')
    # plt.show()
    plt.savefig(f'./EU-15.png', dpi=300)


def error_hn(hn):
    error_msg = ['Request failed', 'socket hang up', 'timeout of', 'disconnected', 'EAI_AGAIN', 'ETIMEDOUT',\
                 'maxContentLength', 'Cannot read properties', 'ECONNRESET']
    for err in error_msg:
        if err in hn:
            return True
    return False
    

if __name__ == '__main__':
    main()
