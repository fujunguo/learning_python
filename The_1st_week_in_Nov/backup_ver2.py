import os
import time

source = ['D:\\Download\\电子原理图']

target_dir = 'E:\\Backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir+os.sep+time.strftime('%y%m%d')

now = time.strftime('%H%M%S')

target = today + os.sep + now + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created dictionary',today)

zip_command = 'zip -r {} {}'.format(target,' '.join(source))

#running the command
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to',target)
else:
    print('Backup failed')
