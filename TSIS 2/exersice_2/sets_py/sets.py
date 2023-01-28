# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Set items are unchangeable, but you can remove and/or add items whenever you like.
# Use {}


thisset = {"apple", "banana", "cherry"}
print(thisset)
#{'cherry', 'banana', 'apple'}

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
# {'banana', 'cherry', 'apple'}

thisset = {"apple", "banana", "cherry"}
print(len(thisset)) # 3

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)
# {'cherry', 'apple', 'banana'}
# {1, 3, 5, 7, 9}
# {False, True}

set1 = {"abc", 34, True, 40, "male"}

print(set1)
# {True, 34, 40, 'male', 'abc'}

thisset = set(("apple", "banana", "cherry"))
print(thisset) #{'banana', 'cherry', 'apple'}
