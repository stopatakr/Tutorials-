import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
data = pd.read_csv('DataFile/contr.csv')

X=np.arange(-500,501,20)
Z=np.arange(0,90,10)

plt.figure(figsize=(25,5))

plt.subplot(2,3,1)
plt.contourf(data)
plt.colorbar(label='Current Density')
plt.title('Filled Contours')

plt.subplot(2,3,2)
plt.contour(X,-Z, data)
plt.colorbar(label='Current Density')
plt.title('Contour Lines')

# Filled Contour Plot with contour lines
plt.subplot(2,3,3)
plt.contourf(X, -Z, data)
plt.colorbar(label='Current Density')
plt.title('Filled Contours with Lines')

# Pseudocolor plot
plt.subplot(2,3,4)
plt.pcolor(X, -Z, data)
plt.colorbar(label='Current Density')
plt.title('Pseudocolor Plot')

# Shaded Surface plot
plt.subplot(2,3,5)
plt.pcolormesh(X, -Z, data, shading='gouraud')
plt.colorbar(label='Current Density')
plt.title('Shaded Surface Plot')

# Image plot
plt.subplot(2,3,6)
plt.imshow(data, extent=[X.min(), X.max(), -Z.max(), -Z.min()])
plt.colorbar(label='Current Density')
plt.title('Image Plot')

plt.show()
