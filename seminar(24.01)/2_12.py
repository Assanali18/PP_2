n = int(input())
m = int(input())
k = int(input())
print('YES' if (k % n == 0 or k % m == 0) and k // (n * m) == 0 else 'NO')
