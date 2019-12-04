
import numpy as np
import matplotlib.pylab as plt

def f(x):
	return np.cos(x)

N = 100000
lista = [np.random.random()*np.pi]
sigma_delta = 1.0

for i in range(1,N):
    propuesta  = lista[i-1] + sigma_delta * (np.random.random()-0.5)
    r = min(1,f(propuesta)/f(lista[i-1]))
    alpha = np.random.random()
    if(alpha<r):
        lista.append(propuesta)
    else:
        lista.append(lista[i-1])
		
x=np.linspace(-5,5,1000)
plt.plot(x, f(x))
_ = plt.hist(lista, density=True, bins=x)
plt.savefig("sigma.png")