import csv
import os, glob
import socket

folder = '2023-4-EU13/cluster-hostnames'
f_paths = glob.glob(os.path.join(f'./{folder}/', '*-hostname.csv'))
for path in f_paths:
    hn_ip_list = []
    with open(path, 'r') as rf:
        reader = csv.reader(rf)
        for row in reader:
            hostname = row[0] + '.abs.hls.ttvnw.net'
            ip = socket.gethostbyname(hostname)
            hn_ip_list.append([hostname, ip])

    cluster = path.split('/')[-1].split('-')[0]
    w_path = f'./{folder}/{cluster}-hn-ip.csv'
    with open(w_path, 'w', newline='') as wf:
        writer = csv.writer(wf)
        writer.writerows(hn_ip_list)
    
    print(f'{cluster} done')
