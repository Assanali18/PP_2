f = open("test.txt", "a")
f.write("It is new line")
f.close()

f = open("test.txt", "r")
print(f.read())
