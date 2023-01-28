thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#{'apple', 'cherry'}

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#{'apple', 'cherry'}

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed random item
print(thisset) #the set after removal
# apple
# {'banana', 'cherry'}

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
# set()


