import json
with open(r"C:\Users\Assan\Downloads\sample-data.json") as inf:
    data = json.load(inf)
print("Interface Status")
print(80*'=')
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")
for i in data["imdata"]:
    print( i["l1PhysIf"]["attributes"]['dn'],"                             ",i["l1PhysIf"]["attributes"]['speed'],'',i["l1PhysIf"]["attributes"]['mtu']) if len(i["l1PhysIf"]["attributes"]['dn']) == 42 else print( i["l1PhysIf"]["attributes"]['dn'],"                              ",i["l1PhysIf"]["attributes"]['speed'],'',i["l1PhysIf"]["attributes"]['mtu'])







