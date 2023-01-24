x = 5
y = "John"
print("*First output*: ")
print (x)
print(y)
###########
x = 4       # x is of type int
x = "Sally" # x is now of type str
print("*Second*: " )
print(x)
###########
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
###########
x, y, z = "Orange", "Banana", "Cherry"
print("*Multiple Variables*: ")
print(x)
print(y)
print(z)
###########
x = y = z = "Orange"
print("*One Value to Multiple Variables*:")
print(x)
print(y)
print(z)
###########
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print("*Unpack a Collection:*")
print(x)
print(y)
print(z)
###########
x = "Python"
y = "is"
z = "awesome"
print("*Output Variables*:")
print(x, y, z)
###########
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
###########
x = 5
y = "John"
print(x, y)
###########
x = "awesome"
print("*Global Variables*:")
def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
###########
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)