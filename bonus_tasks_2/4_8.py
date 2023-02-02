n = int(input())
fct = 1
sum = 0
for i in range(1, n+1):
    fct *= i
    sum += fct
print(sum)
