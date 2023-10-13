import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Definición de variables de entrada
u = 0
k = 7
tao = 8
delta = 1
t = 0
z = []
y = 0
tt = []
uu = []

#Bucle para simulación el sistema en el tiempo
while t <= 1400:
    if t>=5:
        u=10
    if t>=75:
        u=20   
    if t>=145:
        u=30
    if t>=215:
        u=40
    if t>=285:
        u=50
    if t>=355:
        u=45
    if t>=425:
        u=35
    if t>=495:
        u=20
    if t>=565:
        u=0
    if t>=635:
        u=10
    if t>=705:
        u=20   
    if t>=775:
        u=30
    if t>=845:
        u=40
    if t>=915:
        u=50
    if t>=985:
        u=45
    if t>=1055:
        u=35
    if t>=1125:
        u=20
    if t>=1195:
        u=0 
    if t>=1265:
        u=0
#RECORTE DE DATOS        


    y = ((((u * k) - y) * delta) / tao) + y #Ecuación
    uu.append(u)
    z.append(y)
    tt.append(t)
    t = t + 1
    print(y)

print(len(z), len(tt), len(uu))

#Normalización
zmax = max(z)
zmin = min(z)
umax = max(uu)
umin = min(uu)

normu = []
normz = []
for i in range(len(z)):
    nz = (z[i] - zmin) / (zmax - zmin)
    normz.append(nz)
    nu = (uu[i] - umin) / (umax - umin)
    normu.append(nu)

plt.plot(tt, z, color="green")
plt.show()
planta = [uu, z]
planta = np.transpose(planta)



#Se guardan los datos
#np.savez("datos", datos=datos, tt=tt)









