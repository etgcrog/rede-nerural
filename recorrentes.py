from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

base = pd.read_csv('petr4_treinamento.csv')
base = base.dropna()
base_treinamento = base.iloc[:, 1:2].values

normalizador = MinMaxScaler(feature_range=(0,1))
base_treinamento_normalizada = normalizador.fit_transform(base_treinamento)

previsores = []
preco_real = []
for n in range(90, 1242):
    previsores.append(base_treinamento_normalizada[n-90:n, 0])
    preco_real.append(base_treinamento_normalizada[n, 0])
previsores, preco_real = np.array(previsores), np.array(preco_real)
previsores = np.reshape(previsores, (1152, 90, 1))

regressor = Sequential()
regressor.add(LSTM(100, return_sequences=True, input_shape=(90,1)))
regressor.add(Dropout(0.3))
regressor.add(LSTM(50, return_sequences=True))
regressor.add(Dropout(0.3))
regressor.add(LSTM(50, return_sequences=True))
regressor.add(Dropout(0.3))
regressor.add(LSTM(50))
regressor.add(Dropout(0.3))
regressor.add(Dense(1, activation='linear')) #apenas o valor

regressor.compile(optimizer='rmsprop', loss='mean_squared_error',
                  metrics=['mean_absolute_error'])
regressor.fit(previsores, preco_real, epochs=100, batch_size=32)


