import re
txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())  # The first white-space character is located in position: 3


#Split the string at every white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x) #['The', 'rain', 'in', 'Spain']


#Replace all white-space characters with the digit "9":

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)#The9rain9in9Spain


#The search() function returns a Match object:

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)#<_sre.SRE_Match object; span=(5, 7), match='ai'>


