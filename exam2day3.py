import numpy as np
import matplotlib.pyplot as plt
import random

q = []
for k in range(0,5000):
    q.append(random.uniform(1,10))

p = []
for m in range(0,5000):
    p.append(random.uniform(1,10))

qa = 3
pa = 3

qb = 7
pb = 3

qc = 5
pc = 7


def area(x1,x2,x3,y1,y2,y3):
    ar = round(abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))),1)
    return ar

fig, ax = plt.subplots()

tolerance = 0.5  # Numerical tolerance for floating-point comparison

# Separate the points into two groups for efficient plotting
q_in = [q[o] for o in range(len(q)) if abs(area(qa, qb, qc, pa, pb, pc) - 
           (area(qa, qb, q[o], pa, pb, p[o]) + 
            area(qb, qc, q[o], pb, pc, p[o]) + 
            area(qa, qc, q[o], pa, pc, p[o]))) < tolerance]
p_in = [p[o] for o in range(len(q)) if abs(area(qa, qb, qc, pa, pb, pc) - 
           (area(qa, qb, q[o], pa, pb, p[o]) + 
            area(qb, qc, q[o], pb, pc, p[o]) + 
            area(qa, qc, q[o], pa, pc, p[o]))) < tolerance]
q_out = [q[o] for o in range(len(q)) if abs(area(qa, qb, qc, pa, pb, pc) - 
           (area(qa, qb, q[o], pa, pb, p[o]) + 
            area(qb, qc, q[o], pb, pc, p[o]) + 
            area(qa, qc, q[o], pa, pc, p[o]))) >= tolerance]
p_out = [p[o] for o in range(len(q)) if abs(area(qa, qb, qc, pa, pb, pc) - 
           (area(qa, qb, q[o], pa, pb, p[o]) + 
            area(qb, qc, q[o], pb, pc, p[o]) + 
            area(qa, qc, q[o], pa, pc, p[o]))) >= tolerance]
# Plot in a single scatter for each group
ax.scatter(q_in, p_in, color='k')  
ax.scatter(q_out, p_out)  

plt.show()
