import numpy as np
import time as t
import matplotlib.pyplot as plt


Werte = np.loadtxt('240.txt', delimiter='\t', dtype=str )
Werte = np.char.replace(Werte, ',', '.')
Werte = Werte.astype(np.float64)
Array = np.split(Werte, 4, axis=1)

I = np.ravel((-1)*Array[1],  order='C')
T = y = np.ravel(Array[2],  order='C')



x = np.linspace(-3,3,100)
h = 242*x+4.5
z = 407*x+4.5
Error = T*0.03

fig, ax = plt.subplots()
plt.plot(I, T, label='gemessene Werte (Hysteresekurve)',linewidth=2, c='b')
plt.plot(x, z, label='µmax = 407',linewidth=1, c='g')
plt.plot(x, h, label='µA = 242',linewidth=1, c='r')
ax.errorbar(I, y, yerr = Error)
plt.xlim([-3, 3])
plt.ylim([-1000, 1000])
ax.set(xlabel='Stromstärke I in A', ylabel='magnetische Flussdichte B in mT',
       title='Hysteresekurve')

ax.legend()
ax.grid()
fig.savefig("test.png")
plt.show()
