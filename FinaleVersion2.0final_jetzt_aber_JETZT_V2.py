import numpy as np
import time as t
import matplotlib.pyplot as plt


Werte = np.loadtxt('240.txt', delimiter='\t', dtype=str )
Werte = np.char.replace(Werte, ',', '.')
Werte = Werte.astype(np.float64)
Array = np.split(Werte, 4, axis=1)

I = np.ravel((-1)*Array[1],  order='C')
T = y = np.ravel(Array[2],  order='C')
H = 2237*I - 3.56062*T

x = np.linspace(-3300,3300,3000)
h = 0.0432*x+4.5
z = 0.54*x+4.5
Error = T*0.03

fig, ax = plt.subplots()
plt.plot(H, T, label='Hysteresekurve (Messwerte)',linewidth=2, c='b')
plt.plot(x, z, label='µmax = 431.8µ0',linewidth=1, c='g')
plt.plot(x, h, label='µA = 34.4µ0',linewidth=1, c='r')
ax.errorbar(H, y, yerr = Error)
ax.set(xlabel='Feldstärke H in A/m', ylabel='magnetische Flussdichte B in mT',
       title='Hysteresekurve')
ax.set_ylim(-1000, 1000)
ax.set_xlim(-3300, 3300)
ax.legend()
ax.grid()
fig.savefig("FinalesBild.png")
plt.show()
