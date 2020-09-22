import json

with open('interface-data.json') as f:
    data = json.load(f)
def get_result():
    content = data['imdata']
    for i in content:
        dn = i['l1PhysIf']['attributes']['dn']
        speed = i['l1PhysIf']['attributes']['speed']
        mtu = i['l1PhysIf']['attributes']['mtu']
        print(dn, speed, mtu)
def get_content():
    content = data['imdata']
    for i in content:
        access = i['l1PhysIf']['attributes']
        if access['switchingSt'] == 'disabled' and access['layer'] == 'Layer3':
            print(access['dn'])
            
def get_leaf():
    content = data['imdata']
    for i in content:
        access = i['l1PhysIf']['attributes']
        if access['portT'] == 'leaf':
            print(access)
    print("count =",len(access))
def get_max():
    lst = [10, 20, 4, 45, 99, 54, 1, 4, 15]
    lst.sort()
    print("The max integer of the list:",lst[-1])

get_result()
get_content()
get_leaf()
get_max()
