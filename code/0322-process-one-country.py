import csv
import os, glob
import json
from datetime import datetime, timedelta


def main():
    # country_list = ['k1001_100k_nl1033_24R', 'k1002_100k_se597_18R', 'k1003_100k_pl220_22R', 'k1004_100k_at120_24R']
    country_list = ['k1004_100k_at120_24R']
    for c in country_list:
        map_stream_info(c)
        get_server_view(c)
                
            
def map_stream_info(c_path):
    country = c_path.split('_')[2]

    strm_info_list = sorted(glob.glob(os.path.join(f'./{c_path}/dumps/reqStreams/', '*.tsv')))
    pb_list = sorted(glob.glob(os.path.join(f'./{c_path}/info/', '*.tsv')))

    # build a complete info dictionary
    info_dict = dict()
    for path in strm_info_list:
        ft = path.split('/')[-1][:-5]
        pb_time = datetime.fromisoformat(ft[:-4].replace('.', ':') + ft[-4:])

        with open(path, 'r') as f:
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                send_time = datetime.fromisoformat(row[0][:-1])
                http_body = json.loads(row[4])
                for strm in http_body['data']:
                    user_login = strm['user_login']
                    # game_id = strm['game_id']
                    game_name = strm['game_name']
                    viewer_cnt = int(strm['viewer_count'])
                    strm_start_t = strm['started_at']
                    language = strm['language']
                    tags = strm['tags']

                    if user_login not in info_dict:
                        info_dict[user_login] = [[send_time, viewer_cnt, strm_start_t, game_name, language, tags]]
                    else:
                        info_dict[user_login].append([send_time, viewer_cnt, strm_start_t, game_name, language, tags])

    # map stream info to probes
    mk_path = f'./{c_path}/mapped'
    if not os.path.isdir(mk_path):
        os.mkdir(mk_path)

    ttl_probe_cnt = 0
    err_cnt = 0
    vpn_fail_pb_cnt = 0
    vpn_fail_t = []
    # pb_error_msg = ['ERR_BAD_REQUEST', 'ERR_BAD_RESPONSE', 'ECONNRESET', '{}', 'EAI_AGAIN','ETIMEDOUT']
    for path in pb_list:
        ft = path.split('/')[-1][:-5]
        pb_time = datetime.fromisoformat(ft[:-4].replace('.', ':') + ft[-4:])

        fn = path.split('/')[-1]
        with open(path, 'r') as rf:
            reader = csv.reader(rf, delimiter='\t')
            w_path = f'./{c_path}/mapped/{fn}'
            with open(w_path, 'w', newline='') as wf:
                writer = csv.writer(wf, delimiter='\t')
                writer.writerow(['probe_t', 'user_login', 'node', 'user_ip', 'user_country', 'viewer_cnt', 'strm_start_t', 'game_name', 'language', 'tags'])
                for row in reader:
                    ttl_probe_cnt += 1
                    probe_t = datetime.fromisoformat(row[0][:-1])
                    user_login = row[1]

                    # handle error response
                    if row[2][0] != '{':
                        err_cnt += 1
                        continue
                    if 'video-edge' not in row[2]:
                        err_cnt += 1
                        continue

                    try:
                        info = json.loads(row[2])
                        node = info['NODE']
                        user_ip = info['USER-IP']
                        user_country = info['USER-COUNTRY']
                    except:
                        print(f'user login: {user_login} error')
                        return

                    # if user_ip and vpn_ip does not match -> vpn failure
                    '''
                    if user_ip != vpn_ip:
                        vpn_fail_pb_cnt += 1
                        if ft not in vpn_fail_t:
                            vpn_fail_t.append(ft)
                    '''
                    
                    # select the closest earlier stream information to map
                    entry_cnt = len(info_dict[user_login])
                    idx = 0
                    if entry_cnt == 1:
                        idx = 0

                    for i in range(entry_cnt - 1):
                        curr_info = info_dict[user_login][i]
                        next_info = info_dict[user_login][i + 1]
                        next_t = next_info[0]
                        if probe_t > next_t:
                            # last entry
                            if (i + 1) == (entry_cnt - 1):
                                idx = i + 1
                            continue
                        else:
                            idx = i
                            break

                    viewer_cnt = info_dict[user_login][idx][1]
                    strm_start_t = info_dict[user_login][idx][2]
                    game_name = info_dict[user_login][idx][3]
                    language = info_dict[user_login][idx][4]
                    tags = info_dict[user_login][idx][5]

                    writer.writerow([probe_t, user_login, node, user_ip, user_country, viewer_cnt, strm_start_t, game_name, language, tags])
        print(f'{fn} done')
    print(f'{country} done, total probe count: {ttl_probe_cnt}, error count: {err_cnt}')
    print(f'VPN fail probe count: {vpn_fail_pb_cnt}, fail time: {vpn_fail_t}')


def get_server_view(c_path):
    country = c_path.split('_')[2]
    error_msg = ['Request failed', 'socket hang up', 'timeout of', 'disconnected', 'EAI_AGAIN', 'ETIMEDOUT', 'maxContentLength', 'Cannot read properties', 'ECONNRESET']
    
    mk_path = f'./{c_path}/server'
    if not os.path.isdir(mk_path):
        os.mkdir(mk_path)
    
    file_list = sorted(glob.glob(os.path.join(f'./{c_path}/mapped/', '*.tsv')))
    for r_path in file_list:
        hn_dict = dict()
        ft = r_path.split('/')[-1][:-5]
        pb_time = datetime.fromisoformat(ft[:-4].replace('.', ':') + ft[-4:])

        with open(r_path, 'r') as f:
            reader = csv.reader(f, delimiter='\t')
            f.readline()
            for row in reader:
                user_login = row[1]
                hostname = row[2]
                viewer_cnt = int(row[5])
                probe_t = datetime.fromisoformat(row[0])
                strm_start_t = datetime.fromisoformat(row[0][:-3])
                strm_last_t = probe_t - strm_start_t

                # ignore errors in finding hostname
                skip = False
                for err in error_msg:
                    if err in hostname:
                        skip = True
                if skip:
                    continue

                if hostname not in hn_dict:
                    hn_dict[hostname] = [set([user_login]), [viewer_cnt], [strm_last_t], strm_last_t]
                else:
                    hn_dict[hostname][0].add(user_login)
                    hn_dict[hostname][1].append(viewer_cnt)
                    hn_dict[hostname][2].append(strm_last_t)
                    hn_dict[hostname][3] += strm_last_t

        fn = r_path.split('/')[-1]
        w_path = f'./{c_path}/server/{country}-{fn}'
        with open(w_path, 'w', newline='') as f:
            writer = csv.writer(f, delimiter='\t')
            writer.writerow(['hostname', 'unique_channel_cnt', 'max_viewer_cnt', 'avg_viewer_cnt', 'max_strm_last_t', 'avg_strm_last_t'])
            for key, value in hn_dict.items():
                writer.writerow([key, len(value[0]), max(value[1]), sum(value[1])/len(value[1]), max(value[2]), value[3]/len(value[2])])
    print(f'{country} done')


if __name__ == '__main__':
    main()
