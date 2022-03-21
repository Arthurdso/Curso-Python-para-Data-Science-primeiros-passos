from random import randrange
import matplotlib.pyplot as plt


notas_matematica = []


for notas in range(8):
    notas_matematica.append(randrange(0, 9))


x = list(range(1, 9))
y = 10

plt.plot(x, y)
plt.show()

