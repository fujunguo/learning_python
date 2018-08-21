#使用ZIPfile模块列出ZIP文档中的文件
import zipfile

file = zipfile.ZipFile('E:\\Backup\\171030\\152420.zip','r')

#list filenames
for name in file.namelist():
    print(name)

#list file information
for info in file.infolist():
    print(info.filename, info.date_time,info.file_size)
