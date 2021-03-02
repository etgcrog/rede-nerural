import numpy as np
import pandas as pd
import keras

previsores = pd.read_csv("entradas_breast.csv")
classe = pd.read_csv("saidas_breast.csv")

from sklearn.model_selection import train_test_split

previsores_treinamento, previsores_teste, cl_treinamento, cl_teste = train_test_split(previsores, classe, test_size=0.25)

from keras.models import Sequential
from keras.layers import Dense

redeNeural = Sequential()
#CAMADA OCULTA
redeNeural.add(Dense(units = 16, activation='relu', kernel_initializer='random_uniform', input_dim=30)) #INPUT SO NA PRIMEIRA CAMADA
#CAMADA OCULTA
redeNeural.add(Dense(units = 16, activation='relu', kernel_initializer='random_uniform'))
#ULTIMA CAMADA OCULTA
redeNeural.add(Dense(units=1, activation='sigmoid'))

otimizador = keras.optimizers.Adam(lr=0.001, decay=0.001, clipvalue=0.5)

redeNeural.compile(optimizer=otimizador, loss='binary_crossentropy' ,metrics=['binary_accuracy'])
redeNeural.fit(previsores_treinamento, cl_treinamento, batch_size=10, epochs=100)

peso0 = redeNeural.layers[0].get_weights()
print(peso0)

'''previsoes = redeNeural.predict(previsores_teste)
previsoes = (previsoes > 0.5)
from sklearn.metrics import confusion_matrix, accuracy_score
resultados = accuracy_score(cl_teste, previsoes)
matriz_confusao = confusion_matrix(cl_teste, previsoes)'''

resultado = redeNeural.evaluate(previsores_teste, cl_teste)