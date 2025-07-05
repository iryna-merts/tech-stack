# модулі для роботи з файлами та ресурсами операційної системи
import os
import os.path
import glob

ls1 = os.listdir('./fold1')
ls2 = os.listdir('./fold2')

for i in ls1:
    fold_name_1='fold1'
    f_path1 = os.path.join(os.path.abspath('./'+fold_name_1), i)
    size1 = os.path.getsize(f_path1)
    for j in ls2:
        fold_name_2='fold2'
        f_path2 = os.path.join(os.path.abspath('./'+fold_name_2), j)
        size2 = os.path.getsize(f_path2)
        if i==j and size1==size2:
            print('file',i,'in directory',fold_name_1,'has the same size',j,'in directory', fold_name_2)
