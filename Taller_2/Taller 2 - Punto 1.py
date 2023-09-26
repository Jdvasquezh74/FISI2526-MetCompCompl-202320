import numpy as np
import matplotlib.pyplot as plt

Bo = 0.05 #T
f = 7 #Hz
Om = 3.5 #rad/s
Ti = 1/f #s
d = 25 #cm
Re = 1.75 #kO

def DerivadaCentral(f,x,h):
    return (f(x+h) - f(x-h))/(2*h)

def phiB(t):
    return np.pi*((d/2)/100)**2*Bo*np.cos(Om*t)*np.cos(2*np.pi*f*t)

t = np.linspace(0,2*Ti,500)
In = -(1/Re)*DerivadaCentral(phiB,t,0.01)

plt.plot(t,In)
plt.xlabel("Tiempo (s)")
plt.ylabel("Corriente Inducida (A)")
plt.title("Corriente inducida sobre el bucle en función del tiempo")
plt.savefig("Punto1_GraficaIvst.png", format="png",dpi=1000)