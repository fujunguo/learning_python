#使用zipfile模块将文件存储在ZIP文件里

import zipfile
import glob, os

file = zipfile.ZipFile('test.zip','w')

for name in glob.glob('D:\\1\\*'):
    file.write(name,os.path.basename(name), zipfile.ZIP_DEFLATED)

file.close()
