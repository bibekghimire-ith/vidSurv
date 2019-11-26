import os
import shutil


source = os.listdir()

basedir = os.path.abspath(os.path.dirname('__path__'))
dest = os.path.join(basedir, 'static\\images')
# destination = ".\\static\\images"
# print(source)
# print(destination)

for file in source:
    if file.endswith(('.jpg','.txt')):   # Tuple
        print(file)
        # shutil.move(file, dest)
        # shutil.copy(files,destination)
