import numpy as np
import matplotlib.pylab as plt

#Me guie de estas paginas para relaizar la sumatoria
#https://www.nayuki.io/res/how-to-implement-the-discrete-fourier-transform/dft.py
#https://www.nayuki.io/page/how-to-implement-the-discrete-fourier-transform
    
data=np.loadtxt("monthrg.dat")

data1900=data[3481,:]

print (data1900)
def fourier(x):
    n = len(x)
    result = np.ones(n,dtype=complex)
    for i in range(n):  # For each result element
        result[i] = complex(0)
        for t in range(n):  # For each input element
            formula = 2.0j * np.pi * t * i / n
            result[i] += x[t] * np.exp(-1.0*formula)
            
    tam=len(result)
    norm=result/tam
    
    return tam,norm

def F1(w,t):
    f1=3*np.cos(w*t) + 2*np.cos(3*w*t) + np.cos(5*w*t)
    return f1


t=data1900[:,0]
w=data1900[:,3]

tam,val=fourier(F1(w,t))
tf=np.linspace(0,tam,tam)

plt.figure(1,figsize=(14,5))

plt.subplot(1,2,1)
plt.plot(t,w)

plt.xlabel('t')
plt.ylabel('y(t)')
plt.stem(t,abs(val),use_line_collection=True)


plt.savefig('solar.png')