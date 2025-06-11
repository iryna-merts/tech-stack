import csv
import numpy as np
import matplotlib.pyplot as plt
import math
import random
#%matplotlib inline

print("ДЛЯ ДИСКРЕТНОЇ:")
print("\nЗгенерована вибірка:")

range_first= 5
range_last=15
num_of_rand = 20

data=[]
for item in range(num_of_rand):
    data.append(random.randint(range_first, range_last))
for item in range(len(data)):
     print(data[item], end=" ")

# print("\nВибірка з файлу:")
# data = np.loadtxt("Вибірка.txt", delimiter=' ', dtype=np.int)
# for j in range(len(data)):
#     print(data[j], end=" ")


print("Варіаційний ряд:")
data.sort()
for item in range(len(data)):
    print(data[item], end=" ")

n = len(data)
count = 0

# !!!!!!!!!!!! тре розібратися як вона рахує к-ть !!!!!!!!!!!!!!!!!!!

for item in range(n - 1):
    if data[item] != data[item + 1]:
        count += 1
if data[n - 1] != data[n - 2]:
    count += 1

quantity = []
name = []

for item in range(count + 1):
    item = 0
    quantity.append(item)

j = 0
for item in range(n - 1):
    quantity[j] += 1
    if data[item] != data[item + 1]:
        name.append(data[item])
        j += 1
if data[n - 2] != data[n - 1]:
    quantity[j] = quantity[j] + 1
    name.append(data[n - 1])
else:
    name.append(data[n - 1])
    quantity[j] = quantity[j] + 1

print("Варіаційний ряд:")

print("\nX", end='\t|')
for item in range(count + 1):
    print(" ", name[item], end="\t|")
print("   n")

print("V", end='\t|')
for item in range(count + 1):
    print(" ", quantity[item], end="\t|")
print("  ", n)


ind=quantity.index(max(quantity))
Mo=name[ind]

print("Мода: ", Mo)

if n % 2 == 0:
    Me = (data[int((n - 1) / 2)] + data[int((n - 1) / 2) + 1]) / 2

elif n % 2 != 0:
    Me = data[int((n - 1) / 2) + 1]

print("Медіана: ", Me)


av=0
for i in range(count+1):
    av+=name[i]*quantity[i]
average=round(av/n,3)
print("Середнє вибіркове: ", average)


dev=0
for i in range(count+1):
    dev+=quantity[i]* math.pow((name[i]-average),2)
dev=round(dev,3)
print("Девіація: ",dev)


Ro=max(name)-min(name)
print("Розмах: ", Ro)


variansa=dev/(n-1)
print("Варіанса: ", round(variansa,3))


standart=math.sqrt(variansa)
print("Стандарт: ", round(standart,3))


d=dev/n
print("Дисперсія: ", round(d,3))


var=standart/average
print("Варіація: ", round(var, 3))

print("Квантилі:")
if n % 4 == 0:
    print("25: ", data[int((n - 1) / 4)])
else:
    print("25: не існує")

if n % 2 == 0:
    print("50: ", + data[int(2 * (n - 1) / 4)])
else:
    print("50: не існує")

if 3 * n % 4 == 0:
    print("75: ", data[int(3 * (n - 1) / 4)])
else:
    print("75:  не існує")

print("Децилі:")
if n % 10 == 0:
    print("10: ", data[int((n - 1) / 10)])
    print("20: ", data[int(2 * (n - 1) / 10)])
    print("30: ", data[int(3 * (n - 1) / 10)])
    print("40: ", data[int(4 * (n - 1) / 10)])
    print("50: ", data[int(5 * (n - 1) / 10)])
    print("60: ", data[int(6 * (n - 1) / 10)])
    print("70: ", data[int(7 * (n - 1) / 10)])
    print("80: ", data[int(8 * (n - 1) / 10)])
    print("90: ", data[int(9 * (n - 1) / 10)])

elif n % 5 == 0:
    print("20: ", data[int(2 * n / 10)])
    print("40: ", data[int(4 * n / 10)])
    print("60: ", data[int(6 * n / 10)])
    print("80: ", data[int(8 * n / 10)])
    print("10: не існує ")
    print("30: не існує ")
    print("50: не існує ")
    print("70: не існує ")
    print("90: не існує ")

else:
    print("10: не існує ")
    print("20: не існує ")
    print("30: не існує ")
    print("40: не існує ")
    print("50: не існує ")
    print("60: не існує ")
    print("70: не існує ")
    print("80: не існує ")
    print("90: не існує ")


print("Початкові моменти:")
m_1=0
m_2=0
m_3=0
m_4=0

for item in range(n):
    m_1+=data[item]
    m_2+=math.pow(data[item],2)
    m_3+=math.pow(data[item],3)
    m_4+=math.pow(data[item],4)

m_1 /= n
m_2 /= n
m_3 /= n
m_4 /= n

print("M_1 = ",round(m_1,3))
print("M_2 = ",round(m_2,3))
print("M_3 = ",round(m_3,3))
print("M_4 = ",round(m_4,3))

print("Центральні моменти:")
u_1 = 0
u_2 = 0
u_3 = 0
u_4 = 0

for i in range(n):
    u_1 += math.pow((data[i] - average), 1)
    u_2 += math.pow((data[i] - average), 2)
    u_3 += math.pow((data[i] - average), 3)
    u_4 += math.pow((data[i] - average), 4)

u_1 /= n
u_2 /= n
u_3 /= n
u_4 /= n
print("ЦМ_1 = ", round(u1, 3))
print("ЦМ_2 = ", round(u2, 3))
print("ЦМ_3 = ", round(u3, 3))
print("ЦМ_4 = ", round(u4, 3))


M2 = m_2 - m_1 * m_1;
M3 = m_3 - 3 * m_2*m_1 + 2* m_1*m_1*m_1;
M4 = m_4 - 4*m_3*m_1 + 6*m_2*m_1*m_1 - 3* math.pow(m_1,4);

y_1=M3/math.pow(M2,3/2)
y_2=(M4/M2*M2)-3

print("Асиметрія = ", round(y_1,3))
print("Ексцес = ", round(y_2,3))


print("Функція розподілу дискретної змінної")
k=0
for i in range(len(name)):
    if i==0:
        k += quantity[i]
        print("x < ",name[i],", 0")
    else:
        print(name[i-1]," < x < ",name[i],", ",k/n)
        k += quantity[i]
print("x < ",name[len(name)-1],", 1")


emp_1=[]
emp_2=[]
k=0
for item in range(len(name)):
    emp_1.append(name[item])
    emp_1.append(name[item])
    k+=quantity[item]
    emp_2.append(k/n)
    emp_2.append(k/n)

emp_1.pop(0)
emp_1.append(emp_1[len(emp_1)-1])
emp_1.append(emp_1[len(emp_1)-1]+0.1)
emp_2.append(1)

plt.title("Полігон частот дискретної змінної")
plt.plot(name, quantity)
plt.xlabel("Xi", fontsize=18, color="b")
plt.ylabel("Vi", fontsize=18, color="b")
plt.grid(True)


fig = plt.figure()
plt.title("Діаграма частот дискретної зміннох")
markerline, stemlines, baseline = plt.stem(name, quantity, '-.')
plt.xlabel("X_i", fontsize=18)
plt.ylabel("V_i", fontsize=18)
plt.grid(True)

fig = plt.figure()
plt.title("Емпірична функція розподілу дискретної змінної")
plt.plot(emp_1,emp_2)

print("ДЛЯ НЕПЕРЕРВНОЇ:")

r = data[n - 1] - data[0]
k = 0

while math.pow(2, k) < n and math.pow(2, (k + 1)) < n:
    k += 1

d = float(r) / (k + 1)
r_0 = data[0]

c = []
x = []

print("\nКількість проміжків: r + 1 = ", k + 1)
print("Довжина проміжків: ", d)


t = 0
for item in range(k+1):
    item=0
    c.append(item)
    x.append(item)

for item in range(n):
    if data[item] >= r_0 and data[item] < r_0 + d:
        c[t]+=1
    else:
        if data[item] == data[n-1]:
            c[t]+=1
            x[t] = (2 * r_0 + d) / 2
        else:
            x[t] = (2 * r_0 + d) / 2
            r_0 += d
            t+=1
            c[t]+=1

s = 0
for i in range(k + 1):
    s += c[i]

print("\nX", end='\t|')
for i in range(count + 1):
    print(" ", name[i], end="\t|")
print("   n")

print("Z", end='\t|')
for i in range(count + 1):
    print(" ", quantity[i], end="\t|")
print("  ", s)

print("\nЕлементів на проміжку: ")
for i in range(k + 1):
    print(c[i], end="\t")

print("\n\nСердени проміжків:")
for i in range(k + 1):
    print(round(x[i], 2), end="\t")


empn_1 = []
empn_2 = []
k = 0
for i in range(x.__len__()):
    empn_1.append(x[i])
    empn_1.append(x[i])
    k += c[i]
    empn_2.append(k / n)
    empn_2.append(k / n)

empn_1.pop(0)
empn_1.append(empn_1[len(empn_1) - 1])
empn_1.append(empn_1[len(empn_1) - 1] + 0.1)
empn_2.append(1)

print("Функція розподілу неперервної змінної")

k = 0
for i in range(len(x)):
    if i == 0:
        k += c[i]
        print("x < ", x[i], ", 0")
    else:
        print(x[i - 1], " < x < ", x[i], ", ", k / n)
        k += x[i]
print(x[len(x) - 1], " < x , 1")

# !!!!!!!!!!!!!!!!обрахунки!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


fig = plt.figure()
plt.title("Діаграма частот неперервної змінної")
markerline, stemlines, baseline = plt.stem(x, c, '-.')

plt.title("Полігон частот неперервної змінної")
plt.plot(x, c)


plt.figure("Гісторгама частот")
plt.title("Гісторгама частот неперервної змінної")
index = np.arange(len(x))
plt.bar(index, c)
plt.xticks(index, x, fontsize=10, rotation=20)

fig = plt.figure()
plt.title("Гісторгама частот неперервної змінної")
index = np.arange(len(x))
plt.bar(index, c)
plt.xticks(index, x, fontsize=10, rotation=20)

plt.title("Діаграма частот неперервної змінної")
plt.yticks(c)

fig = plt.figure()
plt.title("Емпірична функція розподілу неперервної змінної")
plt.plot(empn_1, empn_2)

plt.show()


