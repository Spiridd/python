import os


os.chdir('/home/dimon')
directories = []
for cur_dir, dirs, files in os.walk('main'):
    containspy = False
    for file in files:
        if '.py' in file:
            containspy = True
            break
    if containspy:
        directories.append(cur_dir)
directories.sort()
[print(dir) for dir in directories]
