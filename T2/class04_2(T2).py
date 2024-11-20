import numpy as np

'''Try in logspace as well'''

z=5
C1C2 = 100
P1P2= 10

rho1=10
rho2=100
k=(rho2-rho1)/(rho2+rho1)

r1=((C1C2)/2)-((P1P2)/2)
r2=C1C2-r1
r4=((C1C2)/2)-((P1P2)/2)
r3=C1C2-r4
rho = (((1/r1)-(1/r2))-((1/r3)-(1/r4)))**(-1)

y=0
for m in range(1,46):
    term1=(1/((r1**2)+(4*m**2*z**2))**0.5)
    term2=(1/((r2**2)+(4*m**2*z**2))**0.5)
    term3=(1/((r3**2)+(4*m**2*z**2))**0.5)
    term4=(1/((r4**2)+(4*m**2*z**2))**0.5)
    y=y+((k**m)*(term1-term2-term3+term4))

rho_final=rho1*(1+(2*rho*y))
print(rho_final)


