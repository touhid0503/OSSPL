import shutil, os

folder1 = "D:/touhid1/"
folder2 = "D:/touhid2/"
filepath = folder1 + "example.py"


if os.path.exists(folder1):
    raise FileExistsError(f"The folder {folder1} already exists!")
else:
    os.makedirs(folder1)

open(filepath, 'w').write('print("Hello")')

if os.path.exists(folder2):
    raise FileExistsError(f"The folder {folder2} already exists!")
else:
    os.makedirs(folder2)

src = filepath
des = folder2
shutil.copy(src, des)
