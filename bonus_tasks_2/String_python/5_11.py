s = input()
a = s[:s.find('h')+1] 
b = s[s.find('h')+1:s.rfind('h')]

b = b.replace('h', 'H')
c = s[s.rfind('h'):]
print(a+b + c)