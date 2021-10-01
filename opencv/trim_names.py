import os
path = "C:/02 - www/opencv_script/fotosadm/ADM"
files = os.listdir(path)


for index, file in enumerate(files):
    sep = ' '
    stripped = file.split(sep, 1)[0]
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([stripped, '.jpg'])))