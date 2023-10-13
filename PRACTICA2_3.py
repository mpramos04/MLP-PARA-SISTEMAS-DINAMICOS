
#from keras.layers.core import Dense
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import random

#Genera los escalones aleatorios
def escalones_aleatorios(k, tao, delta): 
    u = 0
    y = 0
    t = 0
    z = []
    tt = []
    uu = []
    
    while t<=1400: 
            if t % 70 == 0:
               u = random.random() * 100
            
            y =((((u*k)-y)*delta)/tao)+y
            uu.append(u)
            z.append(y)
            tt.append(t)
            t=t+1
            print(y)
            
    
    entradas = list(uu)
    np.savetxt('Entradas.txt', entradas)
    salidas = list(z)
    np.savetxt('Salidas.txt', salidas)
    
    
    tt = np.transpose(tt)
    plt.plot(z, color = "red")
    plt.plot(uu, color = "blue")
    plt.title('Escalones aleatorios')
    plt.legend()
    plt.show()

#Normalización de datos
def Normalizacion(z, uu):
    zmax = max(z)
    zmin = min(z)
    umax = max(uu)
    umin = min(uu)
    
    UZ = list(np.array([umin, umax, zmin, zmax]))
    np.savetxt('UZ.txt', UZ)
    normu = []
    normz = []

    for i in range(len(z)):
        nz = (z[i] - zmin) / (zmax - zmin)
        normz.append(nz)
        nu = (uu[i] - umin) / (umax - umin)
        normu.append(nu)
        
    len_z = len(normz)
    len_u = len(normu)
    return normu, normz, len_z, len_u

#Se carga el modelo de la red neuronal
model = load_model('ModeloOrden1.h5')
print(model.summary())
print("Modelo Cargado!")

#Se generan los escalones y guarda los datos
escalones_aleatorios(7,8, 1)
data = np.array(np.loadtxt('Entradas.txt'))
data1 = np.array(np.loadtxt('Salidas.txt'))
Normalizacion(data1, data)
val_nor = np.array(np.loadtxt('UZ.txt'))
umin = val_nor[0]
umax = val_nor[1]
zmin = val_nor[2]
zmax = val_nor[3]
[normz, normu, len_z, len_u] = Normalizacion(data1, data)

#Predicciones de las salidas usando el modelo
uk = normu
yk = []
for i in range(len(normu)):
    print('Iteracion: ', i)
    if i == 0:                
        vec = 0, 0, 0, 0
        vec = np.array(vec)
        vec = vec[np.newaxis]
        aux = model.predict(vec)
        yk.append(float(np.array(aux)))
        print(yk)
        uk.insert(0, 0) 
    elif i == 1:                
        vec = uk[i - 1], 0, yk[i - 1], 0
        vec = np.array(vec)
        vec = vec[np.newaxis]
        aux = model.predict(vec)
        yk.append(float(np.array(aux)))
        uk.insert(0, uk[i - 1])
    else:
        vec = uk[i - 1], uk[i - 2], yk[i - 1], yk[i - 2]
        vec = np.array(vec)
        vec = vec[np.newaxis]
        aux = model.predict(vec)
        yk.append(float(np.array(aux)))

#Desnormalización de las salidas
yk_m = []
u_m = []
for m in range(len(yk)):
    yk_m.append((zmax - zmin) * yk[m] + zmin)
    u_m.append((umax - umin) * normu[m] + umin)


plt.plot(yk_m, color = 'Red')
plt.plot(data1, color = 'Blue')
plt.title('Salida')
plt.legend(['Salida estimada', 'Salida real'])
plt.show()