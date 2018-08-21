#在脚本中使用zipfile模块而非 os.system调用来实现压缩/备份文件功能
#实现备份的另一种方式
#随时供你在你的电脑上没有 zip程
#序，作为没有外部依赖的情况下使用这些功能。

import zipfile
import glob,os

file = zipfile.ZipFile('E:\\Backup\\backup_new_solution.zip','w')

for name in glob.glob('D:\\Download\\电子原理图\\*'):
    file.write(name,os.path.basename(name),zipfile.ZIP_DEFLATED)
