import os
import os.path

t=str(input('enter file type (txt/py/doc/exe/dll/jpg):'))
tp='.'+t

ls = os.listdir('./fold1') # список всіх файлів і папок, які є в поточній папці
print(ls)

for i in ls:
    ls1=os.listdir('./fold1/'+i)
    for j in ls1:
        root, ext = os.path.splitext(j) #поділити назву файла на назву і розширенн
        if ext==tp:
            print(j)
