import csv
import os, glob
from matplotlib import pyplot as plt

def error_hn(hn):
    error_msg = ['Request failed', 'socket hang up', 'timeout of', 'disconnected', 'EAI_AGAIN', 'ETIMEDOUT',\
                 'maxContentLength', 'Cannot read properties', 'ECONNRESET']
    for err in error_msg:
        if err in hn:
            return True
    return False

main_subnet = {'k5082_100k_25Hz_eu6_48R_1D/k5082_Berlin': 'fra06', \
                'k5081_100k_25Hz_eu15_48R_1D/k5081_Copenhagen': 'mia05', \
                'k5081_100k_25Hz_eu15_48R_1D/k5081_Marseille': 'mrs02', \
                'k5082_100k_25Hz_eu6_48R_1D/k5082_Warsaw': 'waw02', \
                'k5081_100k_25Hz_eu15_48R_1D/k5081_London': 'lhr08', \
                'k5081_100k_25Hz_eu15_48R_1D/k5081_Paris': 'cdg02'}

for path, main_subnet in main_subnet.items():
    file_list = glob.glob(os.path.join(f'./{path}/edgs-w-info-sorted/', '*.csv'))

    backup_cnt_list = [0] * 24
    hour_list = [i for i in range(24)]
    for fn in file_list:
        with open(fn, 'r') as f:
            f.readline()
            reader = csv.reader(f)

            for row in reader:
                hostname = row[2]
                if error_hn(hostname):
                    continue
                subnet = hostname.split('.')[1]
                if subnet != main_subnet:
                    hour = int(row[1][11:13])
                    backup_cnt_list[hour] += 1

    # plot
    city_name = path.split('_')[-1]
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.bar(hour_list, backup_cnt_list)
    ax.grid()
    plt.title(f'{city_name}')
    plt.xlabel('Hour in Day')
    plt.ylabel('# of Backup Servers')
    # plt.show()
    plt.savefig(f'./{path}/{city_name}.png', dpi=300)

