n = int(input())
m = int(input())
x = int(input())
y = int(input())
if n >m:
    n = n + m
    m = n - m
    n = n - m
if 2*x >n:
    x = n - x
if 2 * y > m:
    y = m - y
    
if x < y :
    print(x)
else:
    print(y)
