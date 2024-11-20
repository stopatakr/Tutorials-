import numpy as np
x1 = int(input("Enter x1:"))
z1 = int(input("Enter z1: "))
x2 = int(input("Enter x2:"))
z2 = int(input("Enter z2: "))
x_off = int((input("Enter offset of x: ")))
z_off = int(input("Enter offset of z: "))

term1 = ((x2-x_off)**2+(z2-z_off)**2)/((x1-x_off)**2+(z2-z_off)**2)
term2 = ((x2-x_off)**2+(z1-z_off)**2)/((x1-x_off)**2+(z1-z_off)**2)
term3 = ((x2-x_off)*((z2-z_off)-(z1-z_off)))/((x2-x_off)**2+((z1-z_off)*(z2-z_off)))
term4 = ((x1-x_off)*((z2-z_off)-(z1-z_off)))/((x1-x_off)**2+((z1-z_off)*(z2-z_off)))

H = ((z2-z_off)*np.log(term1))-((z1-z_off)*np.log(term2))+(2*(x2-x_off)*np.arctan(term3))-(2*(x1-x_off)*np.arctan(term4))
print (round(H,2))