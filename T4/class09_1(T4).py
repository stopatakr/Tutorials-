'''
Root mean square error(RMSE)
find error between point in line and actual point of scatter plot, then square that error, then mean all the squared errors,
then root that mf
Age=b1*depth+b0

'''

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

data = np.loadtxt('DataFile/agedepth_1.txt')
X=data[:,0]
Y=data[:,1]

sum=0
sum2=0

for i in range(0,len(X)):
    sum=sum+((X[i]-np.mean(X))*(Y[i]-np.mean(Y)))
    sum2=sum2+((X[i]-np.mean(X))**2)
    
b1=sum/sum2

b0=np.mean(Y)-(b1*np.mean(X))

fig, ax=plt.subplots()

k=X
q=b0+b1*k

ax.scatter(X,Y,color='b',marker='o',edgecolor='k')
ax.plot(k,q)

plt.show()