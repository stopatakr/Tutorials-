import numpy as np
from matplotlib import pyplot as plt

data = np.loadtxt('DataFile/VLFR_data.dat')

a=data[:,0]
b=data[:,1]
c=data[:,2]
d=data[:,3]
e=data[:,4]


'''plt.subplot(121)
plt.plot(a, b, 'r-', label='Real')
plt.plot(a, c, 'k-', label='Imag')
plt.xlabel('Distance (m)', fontsize=14)
plt.ylabel('Anomaly (%)', fontsize=14)
plt.legend(fontsize=12)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()'''


fig, ax1 = plt.subplots(figsize=(6, 6))
ax2 = ax1.twinx()

ax1.plot(a, b, 'r-', label='Real')
ax2.plot(a, c, 'k-', label='Imag')

ax1.set_xlabel('Distance (m)', fontsize=14)
ax1.set_ylabel('Real anomaly', fontsize=14, color='r')
ax2.set_ylabel('Imag anomaly', fontsize=14, color='k')

ax1.tick_params(axis='both', labelsize=14)
ax2.tick_params(axis='both', labelsize=14)

plt.tight_layout()
plt.show()

'''
learn scatterplot by yourself
'''