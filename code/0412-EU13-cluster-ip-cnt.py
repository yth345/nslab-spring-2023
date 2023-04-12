import csv
import os, glob
from matplotlib import pyplot as plt

cluster_ip = dict()

def main():
    path_list = ['k1001_100k_nl1033_24R', 'k1002_100k_se597_18R', 'k1003_100k_pl220_22R', 'k1004_100k_at120_24R', 'k5110_100k_EU13_24R']
    weird_cluster = ['mrs02', 'mil02', 'arn04', 'vie02']
    for path in path_list:
        get_ip_cnt(path)
        print(f'{path} done')
    for key, value in cluster_ip.items():
        print(f'{key}: {len(value)}')
        if key in weird_cluster:
            write_ip(key, value)


def get_ip_cnt(ds_path):
    edgs_fn = glob.glob(os.path.join(f'./{ds_path}/mapped/', '*.tsv'))
    for path in edgs_fn:
        with open(path, 'r') as f:
            f.readline()
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                node = row[2]
                cluster = node.split('.')[-1]
                if cluster in cluster_ip:
                    cluster_ip[cluster].add(node)
                else:
                    cluster_ip[cluster] = set([node])


def write_ip(cluster_name, ips):
    with open(f'./{cluster_name}-hostname.csv', 'w', newline='') as wf:
        writer = csv.writer(wf)
        for ip in ips:
            writer.writerow([ip])


if __name__ == '__main__':
    main()