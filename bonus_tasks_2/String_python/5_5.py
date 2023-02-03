a = input()
if a.find('f') != a.rfind('f'):
    print(a.find('f'), a.rfind('f'))
elif a.find('f') == a.rfind('f') and a.find('f') != -1:
    print (a.find('f'))
else: 
    pass