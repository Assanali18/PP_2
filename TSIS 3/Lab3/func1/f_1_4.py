a = [int(i) for  i in input().split()]
for i in range(2, int((len(a))**0.5)+1): a= list(filter(lambda x: x == i or x % i, a))
print (a)
