print("*Assign String to a Variable*:")
a = "Hello"
print(a)
print()

##############
print("*Multiline Strings*:")
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print()

##############
print("*Strings are Arrays*:")

a = "Hello, World!"
print(a[1])
print()

##############
print("*Looping Through a String*:")

for x in "banana":
  print(x) 
print()

##############
print("*String Length*:")

a = "Hello, World!"
print(len(a))
print()

##############
print("*Check String*:")

txt = "The best things in life are free!"
print("free" in txt)
print()

##############
print("*Check if NOT*:")

txt = "The best things in life are free!"
print("expensive" not in txt)
print()

##############
print("*Check if NOT*:")

txt = "The best things in life are free!"
print("expensive" not in txt)
print()

##############
print("*Slicing*:")

b = "Hello, World!"
print(b[2:5])
print()

##############
print("*Slice From the Start*:")

b = "Hello, World!"
print(b[:5])    
print()

##############
print("*Slice From the End*:")

b = "Hello, World!"
print(b[2:])  
print()

##############
print("*Negative Indexing*:")

b = "Hello, World!"
print(b[-5:-2])
print()

##############
print("*Upper Case*:")

a = "Hello, World!"
print(a.upper())
print()

##############
print("*Lower Case*:")

a = "Hello, World!"
print(a.lower())
print()

##############
print("*Remove Whitespace*:")

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
print()

##############
print("*Replace String*:")

a = "Hello, World!"
print(a.replace("H", "J"))
print()

##############
print("*Split String*:")

a = "Hello, World!"
b = a.split(",")
print(b)

print()

##############
print("*String Concatenation*:")

a = "Hello"
b = "World"
c = a + b
print(c)

print()

##############
print("*String Format*:")

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

print()

##############
print("*String Format*:")

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) 

print()

##############

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) 

print()

##############
print("*Escape Character*:")
txt = "We are the so-called \"Vikings\" from the north."
print(txt) 

print()

##############
print("*Hex value*:")
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

print("*Oct value*:")
txt = "\110\145\154\154\157"
print(txt) 

print()




