import csv
import os, glob
from matplotlib import pyplot as plt

cluster_ip = dict()

def main():
    city_lst_1 = ['Amsterdam', 'Copenhagen', 'Frankfurt', 'London', 'Madrid', 'Marseille', 'Milan', 'Oslo', 'Paris']
    city_lst_2 = ['Berlin', 'Helsinki', 'Prague', 'Stockholm', 'Vienna', 'Warsaw']

    for city in city_lst_1:
        get_ip_cnt(f'k5081_100k_25Hz_eu15_48R_1D/k5081_{city}')
        print(f'{city} done')
    for city in city_lst_2:
        get_ip_cnt(f'k5082_100k_25Hz_eu6_48R_1D/k5082_{city}')
        print(f'{city} done')

    for key, value in cluster_ip.items():
        print(f'{key}: {len(value)}')


def get_ip_cnt(c_path):
    non_eu = ['atl', 'den', 'dfw', 'iad', 'iah', 'jfk', 'lax', 'mia', 'ord', 'pdx', 'phx', 'qro', 'sea', 'sjc', 'slc', 'ymq', 'yto']

    edgs_fn = glob.glob(os.path.join(f'./{c_path}/edgs-w-info-sorted/', '*.csv'))
    for fn in edgs_fn:
        with open(fn, 'r') as f:
            f.readline()
            reader = list(csv.reader(f))
            for row in reader:
                hostname = row[2]
                if error_hn(hostname):
                    continue
                cluster = row[2].split('.')[1]
                hn_seg = row[2].split('.')
                server_code = hn_seg[0][-6:] + '.' + hn_seg[1]
                if server_code[7:10] in non_eu:
                    continue
                if cluster in cluster_ip:
                    cluster_ip[cluster].add(server_code)
                else:
                    cluster_ip[cluster] = set([server_code])


def error_hn(hn):
    error_msg = ['Request failed', 'socket hang up', 'timeout of', 'disconnected', 'EAI_AGAIN', 'ETIMEDOUT',\
                 'maxContentLength', 'Cannot read properties', 'ECONNRESET']
    for err in error_msg:
        if err in hn:
            return True
    return False


if __name__ == '__main__':
    main()