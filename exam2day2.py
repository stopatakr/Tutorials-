import numpy as np
import matplotlib.pyplot as plt
import random

q = []
for k in range(0,5000):
    q.append(random.uniform(1,10))

p = []
for m in range(0,5000):
    p.append(random.uniform(1,10))

cq = 5.5
cp = 5.5
r = 3

fig, ax = plt.subplots()
ax.set_aspect('equal')

# Separate the points into two groups for efficient plotting
q_in = [q[o] for o in range(len(q)) if np.sqrt(((q[o]-cq)**2)+((p[o]-cp)**2))<=r]
p_in = [p[o] for o in range(len(q)) if  np.sqrt(((q[o]-cq)**2)+((p[o]-cp)**2))<=r]
q_out = [q[o] for o in range(len(q)) if not ( np.sqrt(((q[o]-cq)**2)+((p[o]-cp)**2))<=r)]
p_out = [p[o] for o in range(len(q)) if not ( np.sqrt(((q[o]-cq)**2)+((p[o]-cp)**2))<=r)]

# Plot in a single scatter for each group
ax.scatter(q_in, p_in, color='b')  
ax.scatter(q_out, p_out, color='r')  

plt.show()
