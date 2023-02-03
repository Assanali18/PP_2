a = input()
b = a[:int(len(a)/2) + (len(a)+1)%2]
c = a[len(a)/2+1 + (len(a)+1)%2:]
print(b+c)
