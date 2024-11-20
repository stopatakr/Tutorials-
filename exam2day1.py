import numpy as np
import matplotlib.pyplot as plt
import random

q = []
for k in range(0,5000):
    q.append(random.uniform(1,10))

p = []
for m in range(0,5000):
    p.append(random.uniform(1,10))


fig, ax = plt.subplots()

# Separate the points into two groups for efficient plotting
q_in = [q[o] for o in range(len(q)) if 3 <= q[o] <= 8 and 3 <= p[o] <= 8]
p_in = [p[o] for o in range(len(q)) if 3 <= q[o] <= 8 and 3 <= p[o] <= 8]
q_out = [q[o] for o in range(len(q)) if not (3 <= q[o] <= 8 and 3 <= p[o] <= 8)]
p_out = [p[o] for o in range(len(q)) if not (3 <= q[o] <= 8 and 3 <= p[o] <= 8)]

# Plot in a single scatter for each group
ax.scatter(q_in, p_in, color='b')  
ax.scatter(q_out, p_out, color='r')  

plt.show()



