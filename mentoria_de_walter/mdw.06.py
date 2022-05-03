# ¿ Que es matplotlib.pyplot ?
# Instalar matplotlib.pyplot:
# python -m pip install <libreria>
# matplotlib.pyplot

import matplotlib.pyplot as plt

x = []
y = []
for i in range(-25, 25):
  x.append(i)
  y.append(i**2)

x1 = []
y1 = []
for i in range(-25, 25):
  x1.append(i)
  y1.append(abs(i))

plt.plot(x, y, "g^", x1, y1, "r.")
plt.axis([-20, 20, 0, 100])
plt.xlabel("EJE X")
plt.ylabel("EJE Y")
plt.show()
