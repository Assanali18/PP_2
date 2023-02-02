a = int(input())
b = int(input())

if b > a:
    for i in range(a , b+1):
        print (i, end = ' ')
else:
    for i in range(a, b-1, -1):
        print (i, end = ' ')
