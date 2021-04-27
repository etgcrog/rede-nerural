import numpy as np
import pandas as pd
from keras.layers import Dense, Dropout, LSTM
from keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler
import matplotlib as plt

base = pd.read_csv('petr4_treinamento_ex.csv')
base = base.dropna()
base_train = base.iloc[:, 1:2].values

normalizador = MinMaxScaler(feature_range=(0,1))
base_train_normalizada = normalizador.fit_transform(base_train)

previsores = []
preco_real= []
for i in range(90, 1242):
    previsores.append(base_train_normalizada[i-90:i, 0])
    preco_real.append(base_train_normalizada[i, 0])
previsores, preco_real = np.array(previsores), np.array(preco_real)
previsores = np.reshape(previsores, (previsores.shape[0],
                                     previsores.shape[1],1))

regressor = Sequential()
regressor.add(LSTM(units = 100, return_sequences = True, input_shape = (previsores.shape[1], 1)))
regressor.add(Dropout(0.3))

regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units = 50))
regressor.add(Dropout(0.2))

regressor.add(Dense(units = 1, activation = 'linear'))

regressor.compile(optimizer="rmsprop", loss='mean_squared_error', metrics=['mean_absolute_error'])
regressor.fit(previsores, preco_real, epochs = 100, batch_size=32)

base_teste = pd.read_csv('petr4_teste_ex.csv')
base_test  = base_teste.iloc[:, 1:2].values

completa = pd.concat((base['Open'], base_test['Open']), axis=0)
entradas = completa[len(completa)-len(base_test) - 90:].values
entradas = entradas.reshape(-1, 1)
entradas = normalizador.transform(entradas)

teste = list()
for i in range (90, 112):
    teste.append(entradas[i-90:i, 0])
teste = np.array(teste)
teste = np.reshape(teste, (teste.shape[0], teste.shape[1], 1))
futuras = regressor.predict(teste)
futuras = normalizador.inverse_transform(futuras)

plt.plot(preco_real_teste, color = 'red', label = 'Preço real')
plt.plot(previsoes, color = 'blue', label = 'Previsões')
plt.title('Previsão preço das ações')
plt.xlabel('Tempo')
plt.ylabel('Valor Yahoo')
plt.legend()
plt.show()


