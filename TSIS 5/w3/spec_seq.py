import re

txt = "The rain in Spain"

#Check if the string starts with "The":

x = re.findall("\AThe", txt)

print(x)

if x:
  print("Yes, there is a match!")
    #['The']
    #Yes, there is a match!
else:
  print("No match")


txt = "The rain in Spain"

#Check if "ain" is present at the beginning of a WORD:

x = re.findall(r"\bain", txt)

print(x) #[]

if x:
  print("Yes, there is at least one match!") 
else:
  print("No match")

  txt = "The rain in Spain"

#Check if "ain" is present at the end of a WORD:

x = re.findall(r"ain\b", txt)

print(x) #['ain', 'ain']

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


txt = "The rain in Spain"

#Check if "ain" is present, but NOT at the beginning of a word:

x = re.findall(r"\Bain", txt)

print(x) #['ain', 'ain']

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


x = re.findall("\d", txt)
print(x) #[]

x = re.findall("\D", txt)
print(x)#['T', 'h', 'e', ' ', 'r', 'a', 'i', 'n', ' ', 'i', 'n', ' ', 'S', 'p', 'a', 'i', 'n']

x = re.findall("\S", txt)
print(x)#['T', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 'S', 'p', 'a', 'i', 'n']

x = re.findall("\w", txt)
print(x)#['T', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 'S', 'p', 'a', 'i', 'n']


x = re.findall("\W", txt)
print(x)#[' ', ' ', ' ']





