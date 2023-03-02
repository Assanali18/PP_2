import mymodule
mymodule.greeting("Jonathan")# Hello, Jonathan

a = mymodule.person1["age"]
print(a)#36

import mymodule as mx
a = mx.person1["age"]
print(a) #36
####
import platform
x = platform.system()
print(x)# Windows
#####
import platform
x = dir(platform)
print(x)
#####
from mymodule import person1

print(person1["age"])#36


