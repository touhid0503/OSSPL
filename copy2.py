import shutil,os

folder1 = 'touhid/'
file_path1 = folder1 + 'example.txt'

os.makedirs('touhid', exist_ok=True)

open(file_path1, 'w')

folder2 = 'touhid1/'

os.makedirs('touhid1', exist_ok=True)

source_file = 'touhid/example.txt'
destination_dir = 'touhid1'

shutil.copy(source_file, destination_dir)



