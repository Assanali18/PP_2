a = input()
for i in range(len(a)):
    if i % 3 == 0:
        a = a.replace(a[i], ' ', 1)
        i =0
for i in a:
    if i == ' ':
        a = a.replace(i, '', 1)
print(a)