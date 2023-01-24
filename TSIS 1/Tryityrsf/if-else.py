print("*Python Conditions and If statements*")
a = 33
b = 200
if b > a:
  print("b is greater than a")
print()
#########
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
print()
#########
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
print()
#######
if a > b: print("a is greater than b")
print()
########
a = 2
b = 330
print("A") if a > b else print("B")
print()
########
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
print()
########
a = 33
b = 200

if b > a:
  pass
