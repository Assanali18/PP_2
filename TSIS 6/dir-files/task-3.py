import os
PathName = input("Enter yout path:")
path = r"{}".format(PathName)
if os.path.exists(path): 
    print("Your path exist!")
    print("Filename of this path: {}".format(os.path.basename(path)))
    print("Direcory of this path: {}".format(os.path.dirname(path)))
else: print("Your path don't exist ")



