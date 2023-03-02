import re
x =input() 
pattern = re.search(r"\"?([-a-zA-Z0-9.`?]+@\.+\.\w+)\"?" , x)
if pattern:
    print(1)
else: print(2)  