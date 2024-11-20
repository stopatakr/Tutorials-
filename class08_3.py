import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_excel('DataFile/data1.xlsx',names=["A","B","C","D","E","F"])
#plt.figure(figsize=(20,5))

plt.subplot(3,2,1)
plt.hist(data.iloc[:,0],bins='auto',edgecolor='black')
plt.xlabel('Radius(m)')

plt.subplot(3,2,2)
plt.hist(data.iloc[:,1], bins='auto', edgecolor='black')
plt.xlabel('\u03C3 (gm/cc)')  # Sigma symbol

# Subplot 3: Depth
plt.subplot(3,2,3)
plt.hist(data.iloc[:, 2], bins='auto', edgecolor='black')
plt.xlabel('Depth (m)')

# Subplot 4: Location
plt.subplot(3,2,4)
plt.hist(data.iloc[:, 3])
plt.xlabel('Location (m)')

# Subplot 5: Misfit
plt.subplot(3,2,5)
plt.hist(data.iloc[:, 5], bins='auto', edgecolor='black')
plt.xlabel('Misfit')

plt.tight_layout()
plt.show()