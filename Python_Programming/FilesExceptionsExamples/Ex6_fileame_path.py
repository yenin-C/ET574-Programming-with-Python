# The os module provides functions
# for working with files and directories
# (“os” stands for “operating system”).
# os.getcwd returns the name of the current directory
import os
cwd = os.getcwd()
print(cwd)

# A string like cwd that identifies a file is called a path.
# A relative path  starts from the current directory;
# an absolute path starts from the topmost directory in the file system.

print("os.path.abspath('un.txt'):",os.path.abspath('un.txt'))
print("os.path.exists('un.txt'):",os.path.exists('un.txt'))
print("os.path.exists:('abc.txt')",os.path.exists('abc.txt'))

print("os.path.isdir:",os.path.isdir('myfolder'))
print("os.path.isdir:",os.path.isdir('abc'))

fileList = os.listdir(cwd)
print("Current files in the folder:\n",fileList)
