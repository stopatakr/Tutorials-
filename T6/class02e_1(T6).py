import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def schlum(s):
    data=pd.read_excel('data.xlsx',header=None)

    rho = np.array([500,10,5000])
    h = np.array([10,5,999999])
    a= data.iloc[:,0]
    f= data.iloc[:,1]

    lam = []
    for j in range(0,len(a)):
        lam.append(10**((a[j])-(np.log10(s))))

    T = np.zeros((len(rho),len(a)))
    
    for n in range (0,len(T)):
        if n==len(T)-1:
            T[n]=rho[n]
        else:
            continue

    for q in range(len(T)-2,-1,-1):
        for l in range(0,len(lam)):
            T[q][l] = (T[q+1][l]+(rho[q]*(np.tanh(lam[l]*h[q]))))/(1+(((T[q+1][l])*(np.tanh(lam[l]*h[q])))/rho[q]))
        

    rho_a = np.zeros((3,1))

    for u in range(0,len(T)):
        for y in range(0,len(lam)):
            rho_a[u][0] = rho_a[u][0]+(f[y]*T[u][y])
        
    return rho_a[0]


s = [1.5,2,3,4,6,8,10,15,20,25,30,40,50,60,80,100,120,140,160,180,200,250,300,350,400,500,600,800,1000]
pa = []

for r in range(0,len(s)):
    pa.append(schlum(s[r]))

fig, ax = plt.subplots()
ax.plot(s,pa, color='k')
ax.set_title("Electrode Distance vs Apparent Resistivity")
ax.set_xlabel("Electrode Distance-->")
ax.set_ylabel("Apparent Resistivity of Layer 1-->")
plt.grid(True)
plt.show()