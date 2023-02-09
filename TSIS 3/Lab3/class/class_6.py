a, size = [], int(input('Size of list: '))
for i in range(size): a.append(int(input()))
for i in range(2, int((size)**0.5)+1): a= list(filter(lambda x: x != i and x % i==0, a))
print (a)


