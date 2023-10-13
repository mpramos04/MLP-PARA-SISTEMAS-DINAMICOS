import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
#from keras.models import Sequential, model_from_json
#from keras.layers.core import Dense

#Se cargan los datos
array = np.load("datos.npz")
datos = array["datos"]

entrada = (datos[:,0:4])
salida = (datos[:,4])

#Datos de entrenamiento
training_data = entrada
target_data = salida

#Entrenamiento
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(18, input_dim=4, activation='elu'))
model.add(tf.keras.layers.Dense(10, activation='tanh'))
model.add(tf.keras.layers.Dense(1, activation='tanh')) 

model.compile(loss='mean_squared_error',
              optimizer='adam',
              metrics=['binary_accuracy'])

model.fit(training_data, target_data, epochs=1000)
predicciones = model.predict(training_data)

error = np.mean(np.square(predicciones - salida))
print("El error es: ", error)
print(predicciones)

#Se guarda el modelo entrenado
model.save("ModeloOrden1.h5")
print("Modelo Guardado!")

plt.figure(figsize=(10, 6))
plt.plot(target_data, label='Salida Real', color = 'green')
plt.plot(predicciones, label='Salida Estimada', color="red")
plt.xlabel('Muestras')
plt.ylabel('Escalones')
plt.title('Comparación de Salida Estimada y Real')
plt.legend()
plt.show()


# serializar el modelo a JSON
#model_json = model.to_json()
#with open("model.json", "w") as json_file:
 #   json_file.write(model_json)

# serializar los pesos a HDF5



