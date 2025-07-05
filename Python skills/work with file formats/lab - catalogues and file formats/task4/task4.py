# модулі для роботи з файлами та ресурсами операційної системи
import os
import os.path

import shutil #для переміщення файлу

ls = os.listdir('.') # список всіх файлів і папок, які є в поточній папці
print(ls)

for i in ls:
    dirname1 = os.path.abspath('.') # шлях від кореня до поточної папки
    path_to_file = os.path.join(dirname1, i)
    #print(path_to_file)
    root, ext = os.path.splitext(i) #поділити назву файла на назву і розширенн
    if ext=='.jpg':
        new_path_to_file=dirname1+r'\fold1'
        #print(new_path_to_file)
        shutil.move(path_to_file,new_path_to_file)
    if ext=='.txt':
        new_path_to_file=dirname1+r'\fold2'
        #print(new_path_to_file)
        shutil.move(path_to_file,new_path_to_file)
    if ext=='.doc':
        new_path_to_file=dirname1+r'\fold3'
        #print(new_path_to_file)
        shutil.move(path_to_file,new_path_to_file)        
