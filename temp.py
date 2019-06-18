import os


path = '/home/about/me/'




path = os.path.normpath(path)
print(path.split(os.sep))

