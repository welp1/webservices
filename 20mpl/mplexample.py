# ОО подход, методы объектов Figure или AxesSubplot
import matplotlib
print(matplotlib.get_backend())

from matplotlib import pyplot as plt

fig = plt.figure(figsize=(10,4)) # контейнер, а внутри него:
ax1 = fig.add_subplot(1, 2, 1)   # в сетке 1x2 первый график
ax2 = fig.add_subplot(1, 2, 2)   # в сетке 1x2 второй график

fig.set(facecolor = 'green')
fig.suptitle('Это - figure')

ax1.set(title = 'Это - оси ax_1', facecolor='#fff0f0')
ax1.set_xlabel('время')
ax1.set_ylabel('деньги')
ax1.grid(True)
ax1.plot([0, 1, 2, 3, 4], [0, 6, 7, 15, 19])

ax2.set(title = 'Это - оси ax_2', xticks=[], yticks=[], facecolor='#f0f0ff')
ax2.set_xlabel('площадь')
ax2.set_ylabel('урожай')
ax2.scatter([0, 1, 2, 3, 4], [1, 3, 8, 12, 27], color = 'orange')

plt.show()
