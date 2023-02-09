# b = sqrt( [ (x1^2 + x2^2 + ...) - 2s(x1+x2+....) + cnt*s^2] / cnt-1)
n, sum, sum1, cnt = int(input()), 0, 0, 0
while n:
    sum1, sum, cnt = sum1+ n**2, sum + n, cnt+1
    n = int(input())
print(((sum1 - 2*sum/cnt*sum + cnt * (sum/cnt)**2) / (cnt -1))**0.5)
