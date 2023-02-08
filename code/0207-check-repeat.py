import csv

######### Change Here ###############
main_city = ['k5081_Amsterdam']
other_city = ['k5082_Berlin', 'k5081_Frankfurt', 'k5081_Oslo', 'k5081_Paris', 'k5082_Warsaw']
target_subnet = 'ams02'
#####################################

def get_subnet_set(path, option, main_set, other_set):
    with open(path, 'r') as f:
        f.readline()
        reader = csv.reader(f)
        for row in reader:
            sv_code = row[0].split('.')
            if sv_code[0] == target_subnet:
                if option == 'main':
                    main_set.add(sv_code[1])
                elif option == 'other':
                    other_set.add(sv_code[1])


main_server_set = set()
other_server_set = set()

for mc in main_city:
    path = f'code/2023-EU15/{mc}/unique-ch-cnt-sorted.csv'
    get_subnet_set(path, 'main', main_server_set, other_server_set)
for oc in other_city:
    path = f'code/2023-EU15/{oc}/unique-ch-cnt-sorted.csv'
    get_subnet_set(path, 'other', main_server_set, other_server_set)
print(f'len(main_set): {len(main_server_set)}, len(other_set): {len(other_server_set)}')

diff_cnt = len(other_server_set - main_server_set)
if diff_cnt == 0:
    print('complete cover')
else:
    print('different amount:', diff_cnt)