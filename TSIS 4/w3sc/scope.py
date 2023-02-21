def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc() #300
########

x = 300
def myfunc():
  print(x)
myfunc()
print(x)
#300
#300
#######

x = 300
def myfunc():
  x = 200
  print(x)
myfunc()
#200
print(x)
#300
########

def myfunc():
  global x
  x = 300

myfunc()
print(x)
#300
##########

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)
#200