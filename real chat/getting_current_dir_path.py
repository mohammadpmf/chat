# Excellent :D
import os
cwd = os.getcwd()
print(cwd)

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
# print(__file__)
open(f"{dir_path}/test.txt", 'x')
