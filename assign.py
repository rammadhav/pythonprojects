import json

with open('interface-data.json') as f:
    data = json.load(f)
def get_result():
    content = data['imdata']
    name = list(map(lambda x : x['l1PhysIf']['attributes'],content))
    for i in name:
        dn = i['dn']
        speed = i['speed']
        mtu = ['mtu']
        print(dn, speed, mtu)
def get_content():
    content = data['imdata']
    name = list(map(lambda x: x['l1PhysIf']['attributes'], content))
    for i in name:
        if i['switchingSt'] == 'disabled' and i['layer'] == 'Layer3':
            print(i['dn'])
            
def get_leaf():
    content = data['imdata']
    count = 0
    name = list(map(lambda x : x['l1PhysIf']['attributes'],content))
    for i in name:
        if i['portT'] == 'leaf':
            count +=1
    print("Number of objects: ",count)

def get_max():
    lst = [10, 20, 4, 45, 99, 104, 1, 4, 15]
    n = len(lst)
    for i in range (n):
        maxnum = i
        for j in range (i,n):
            if lst[j] < lst[maxnum]:
                maxnum =j
        temp = lst[i]
        lst[i] = lst[maxnum]
        lst[maxnum] = temp
    print("The max integer of the list:",lst[-1])

get_result()
get_content()
get_leaf()
get_max()
