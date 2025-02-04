import os
import shutil

folder1 = "E:/7th SEM/OSSPL code/folder1/"
folder2 = "E:/7th SEM/OSSPL code/folder2/"
filepath1 = folder1 + "example1.txt"
filepath2 = folder2 + "example2.txt"


if os.path.exists(folder1):
    raise FileExistsError(f"The folder {folder1} already exists!")
else:
    os.makedirs(folder1)

open(filepath1, "w").write("Hello, World!")

if os.path.exists(folder2):
    raise FileExistsError(f"The folder {folder2} already exists!")
else:
    os.makedirs(folder2)

open(filepath2, "w")

with open(filepath1, "r") as f1:
    content = f1.read()

with open(filepath2, "w") as f2:
    f2.write(content)

print(f"File copied from {filepath1} to {filepath2}")
