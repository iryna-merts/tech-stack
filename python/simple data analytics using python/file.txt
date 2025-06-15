import matplotlib.pyplot as plt
%matplotlib inline

labels = 'Горіхи', 'Сливи', 'Вишні', 'Яблука', 'Полуниця', 'Смородина', 'Малина', 'Суниця'
sizes = [ 2, 20, 25, 50, 10, 8, 8, 5]
explode = (0.1, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct= lambda p: "{:.0f} kg".format(p * sum(sizes) / 100),
        shadow=True, startangle=45)
ax1.axis('equal')

plt.show()
