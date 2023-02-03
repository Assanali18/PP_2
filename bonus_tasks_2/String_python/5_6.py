a = input()
if a.find('f') == -1: print(-2)
else:
    pos = a.find('f')
    print( a.find('f', pos+1))
