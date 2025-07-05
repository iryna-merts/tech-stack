
# модулі для роботи з файлами та ресурсами операційної системи
import os
import os.path
import glob


#модулі для роботи з часом
import datetime # розділені показники часу
import time

#print("Сьогодні: рік {0}, місяць {1}, день {2}".format(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day))

ls = os.listdir('.') # список всіх файлів і папок, які є в поточній папці
#print(ls)

list_of_files = []
for i in ls:
    #print(i)
    timediff = time.time() - os.path.getmtime(i) # обчислюємо різницю в часі
    diff = time.localtime(timediff) # переводимо в структуровану форму
    basetime = time.localtime(os.times().user) # віднімаємо базовий час системи
    mins = diff.tm_min-basetime.tm_min
    secs = diff.tm_sec-basetime.tm_sec
    file_info = dict(zip(['name','mins','secs'],[i,mins,secs])) #assign keys for every line's values
    list_of_files.append(file_info)
print('Файли були створені стільки часу назад:', list_of_files)

ls.sort(key=os.path.getmtime) # сортування за датою створення
print('Усі файли, посортовані за часом створення:')
print("\n".join(ls))

print('Найдавніші 2:', ls[0],ls[1])
print('Найнещодавніші 2:', ls[-1],ls[-2])

