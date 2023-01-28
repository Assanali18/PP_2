#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

thislist = ('apple', 'banana', 'cherry', 'apple', 'cherry')
print(thislist) #('apple', 'banana', 'cherry', 'apple', 'cherry')

thislist = ('apple', 'banana', 'cherry')
print(len(thislist)) # 3

thistuple = ('apple',)
print(type(thistuple)) #<class 'tuple'>

#NOT a tuple
thistuple = ('apple')
print(type(thistuple)) #<class 'str'>


list1 = ('apple', 'banana', 'cherry')
list2 = (1, 5, 7, 9, 3)
list3 = (True, False, False)

print(list1)
print(list2)
print(list3)
# ('apple', 'banana', 'cherry')
# (1, 5, 7, 9, 3)
# (True, False, False)

tuple1 = ('abc', 34, True, 40, 'male')
print(tuple1)
# ('abc', 34, True, 40, 'male')

mytuple = ('apple', 'banana', 'cherry')
print(type(mytuple)) # <class 'tuple'>

thistuple = tuple(('apple', 'banana', 'cherry'))
print(thistuple) # ('apple', 'banana', 'cherry')




