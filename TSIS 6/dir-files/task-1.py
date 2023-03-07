import os
path = r"C:\PP2_tasks\TSIS 4\Lab 4"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
print(dir_list)

print("Directories in '", path, "' :")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])

print("Files in '", path, "' :")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name))])


