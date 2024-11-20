'''
forward differentiation: y=f(x); take different values of x (lets say 0 to 1000 in steps of 10), then calc values of y
plot curve; there's also central and backward; going back to fd, FD=(f(i+1)-f(i)/x(i+1)-x(i)), limit: cannot compute last value

backward differentiation; f`(i)= f(i-1)-f(i)/x(i-1)-x(i)

central differentiation; f`(i)=f(i+1)-f(i-1)/x(i+1)-x(i-1)


'''

import numpy as np
from matplotlib import pyplot as plt

x= np.arange(0,1001,10)
x1 = 400
x2 = 440
z1 = 20
z2 = 40
k = 100
y= k*np.log((((x-x1)**2)+z1**2)/(((x-x2)**2)+z2**2))

G=[]
for q in range(0,len(x)-1):
    G.append((y[q+1]-y[q])/(x[q+1]-x[q]))

G = G+ [G[0]] 


fig, ax1 = plt.subplots()

ax1.plot(x, y)
ax1.set_ylabel("SP Anomaly(mV)")
ax1.set_xlabel("Distance(m)")
ax2 = ax1.twinx()
ax2.plot(x, G, color='orange')
ax2.set_ylabel("SP Gradient(mV/m)")
plt.title("Anomaly Plot")
plt.show()


