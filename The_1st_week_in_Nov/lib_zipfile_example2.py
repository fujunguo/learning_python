#read data from the .zip file

import zipfile
file = zipfile.ZipFile('E:\\Backup20171027200142.zip','r')

for name in file.namelist():
    data = file.read(name)
    print(name, len(data), repr(data[:10]))
