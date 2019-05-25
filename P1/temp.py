import os

dir_list = ['.\\testdir']
dir_list += os.listdir('.\\testdir')

print(dir_list)
