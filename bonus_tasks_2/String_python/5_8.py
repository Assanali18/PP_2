a = input()
if a.find('h') == 0:
    a1 = a[a.rfind('h')-1: a.find('h'): -1]
    print(a[:a.find('h')+1]+ a1 + a[a.rfind('h'):])
else:
    a1 = a[a.rfind('h')-1: a.find('h')-1: -1]
    print(a[:a.find('h')+1]+ a1 + a[a.rfind('h')+1:])