import numpy as np
import matplotlib.pyplot as plt

def curve(t,rho,h):
    t=np.logspace(-1, 4, 60)
    Pa=[]
    phi=[]
    for bb in range(0,len(t)):
        l=len(rho)
        omega=(2*np.pi)/t[bb]
        mu=mu_not=4*np.pi*10**(-7)
        k=np.sqrt(omega*mu*1j)

        T=[]
        S=[]
        for s in range(0,l):
            T.append((k*np.sqrt(rho[s]))*np.tanh((k*h[s])/np.sqrt(rho[s])))
            S.append((1/(k*np.sqrt(rho[s])))*np.tanh((k*h[s])/np.sqrt(rho[s])))

        Z=np.zeros(l, dtype=complex)
        Z[l-1]=k*np.sqrt(rho[l-1])
        for m in range(l-2,-1,-1):
            Z[m]=(Z[m+1]+T[m])/(1+(S[m]*Z[m+1]))          
        Pa.append((1/(omega*mu))*np.abs(Z[0])**2)
        phi.append(np.degrees(np.arctan(np.imag(Z[0])/np.real(Z[0]))))
    return Pa, phi

t = np.logspace(-1, 4, 60)
rho_1 = [490, 490, 27, 27]
rho_2 = [490, 490, 27, 27]
h_1 = [22000, 25000, 40000, 99999999]
h_2= [25000, 25000, 40000, 99999999]
app_1,phase_1=curve(t,rho_1,h_1)
app_2,phase_2=curve(t,rho_2,h_2)

fig,axs=plt.subplots(2)

axs[0].loglog(t,app_1, color='red')
axs[0].loglog(t,app_2, color='blue')
axs[0].grid(True, which='both', ls='--')
axs[0].set_xlabel("Time Period")
axs[0].set_ylabel("Apparent Resistivity")

axs[1].loglog(t,phase_1, color='red')
axs[1].loglog(t,phase_2, color='blue')
axs[1].grid(True, which='both', ls='--')
axs[1].set_xlabel("Time Period")
axs[1].set_ylabel("Phase")

plt.show()
