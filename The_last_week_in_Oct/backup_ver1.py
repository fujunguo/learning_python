import os
import time

source = ['D:\\1']  #需要备份文件的源文件夹

# 除了使用双反斜杠转义序列，你还可以使用原始字符串。
# 例如使用 'C:\\Documents' 或r'C:\Documents' 。
# 然而，不要使用 'C:\Documents' ，
# 因为它将被识别为你使用了一个
# 未知的转义序列 \D 来结束路径的输入。
target_dir = 'E:\\Backup'   #目标文件夹

# 要注意 os.sep 变量的使用方式——它将根据你的操作系统给出相应的分隔符，
# 在GNU/Linux 与 Unix 中它会是 '/' ，在 Windows 中它会是 '\\' ，
# 在 Mac OS 中它会是':' 。使用 os.sep而非直接使用这些字符
# 有助于使我们的程序变得可移植，从而可以在上述这些系统中都能正常工作。

target = target_dir+os.sep +\
         time.strftime('%Y%m%d%H%M%S')+'.zip'
#压缩成Zip格式，其文件名由当前日期与时间组成


if not os.path.exists(target_dir):
    os.mkdir(target_dir)    #如果目标文件夹不存在，则进行创建

zip_command = 'zip -r {0} {1}'.format(target,
                                    ' '.join(source))

#运行备份指令
print('Zip command is:')
print(zip_command)
print('Running:')

# 下面使用了 os.system 函数的命令，这一函数可以使命令像是从系
# 统中运行的。也就是说，从 shell 中运行的——如果运行成功，
# 它将返回 0 ，如果运行失败，将返回一个错误代码。
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')

