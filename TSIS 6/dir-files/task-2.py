import os
print('Exist:', os.access(r'C:\PP2_tasks\TSIS 6\lab 6\dir-files\task-1.py', os.F_OK))
print('Readable:', os.access(r'C:\PP2_tasks\TSIS 6\lab 6\dir-files\task-1.py', os.R_OK))
print('Writable:', os.access(r'C:\PP2_tasks\TSIS 6\lab 6\dir-files\task-1.py', os.W_OK))
print('Executable:', os.access(r'C:\PP2_tasks\TSIS 6\lab 6\dir-files\task-1.py', os.X_OK))