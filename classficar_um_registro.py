import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout

previsores = pd.read_csv("entradas_breast.csv")
classes = pd.read_csv("saidas_breast.csv")


redeNeural = Sequential()
redeNeural.add(Dense(units=8, activation='relu', kernel_initializer='normal', input_dim=30))
#   As entradas não definidas como 0 são aumentadas em 1 / (1 - taxa) 
#   de forma que a soma de todas as entradas permaneça inalterada.
redeNeural.add(Dropout(0.2))
redeNeural.add(Dense(units=8, activation='relu', kernel_initializer='normal', input_dim=30))
redeNeural.add(Dropout(0.2))
redeNeural.add(Dense(units=1, activation='sigmoid'))

#optimizador = keras.optimizers.Adam(lr=0.001, decay=0.001, clipvalue=0.5)
redeNeural.compile(optimizer='adam', loss='binary_crossentropy', metrics=['binary_accuracy'])
redeNeural.fit(previsores, classes, batch_size=10, epochs=100)

#NOVA IMAGEM

novo = np.array([[15.80, 8.34, 118, 0.25, 15.42, 16.8, 70.4, 2.23, 2.21,
                  0.025, 0.14, 0.005, 1098, 0.87, 0.185, 0.215, 178.5, 2022,
                  0.001, 512, 0.04, 0.888, 2.45, 3.15, 4, 98.52, 0.007, 26.5,
                  30, 0.336]])

previsao = redeNeural.predict(novo)
previsao = (previsao > 0.8)










