# __author__: William Kwok
import shutil, os
f1 = open('note', encoding='utf-8')
f2 = open('note1', 'w', encoding='utf-8')
shutil.copyfileobj(f1, f2)

shutil.copyfile('note', 'note2')

file_dir = os.path.dirname(os.path.abspath(__file__))
shutil.make_archive('www', 'zip', file_dir)