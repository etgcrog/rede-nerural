from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

from keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint

base = pd.read_csv('petr4_treinamento.csv')
base = base.dropna()
treinamento = base.iloc[:, 1:7].values

normalizador = MinMaxScaler(feature_range=(0,1))
treinamento_norm = normalizador.fit_transform(treinamento)

normalizador_previsao = MinMaxScaler(feature_range=(0,1))
normalizador_previsao.fit_transform(treinamento[:, 0:1])

previsores = []
preco = []
for i in range(90, 1242):
    previsores.append(treinamento_norm[i-90:i, 0:6])
    preco.append(treinamento_norm[i, 0])
previsores, preco = np.array(previsores), np.array(preco)


redeNeural = Sequential()
redeNeural.add(LSTM(units=100, return_sequences=True, input_shape=(previsores.shape[1], 6)))
redeNeural.add(Dropout(0.3))
redeNeural.add(LSTM(units=50, return_sequences=True))
redeNeural.add(Dropout(0.3))
redeNeural.add(LSTM(units=50))
redeNeural.add(Dropout(0.3))
redeNeural.add(Dense(1, 'sigmoid'))
redeNeural.compile(optimizer='adam', loss='mean_squared_error', metrics=['mean_absolute_error'])

stopping = EarlyStopping(monitor='loss', min_delta=1e-10, patience=10, verbose = 1)
rlr = ReduceLROnPlateau(monitor='loss', factor=0.2, patience=5, verbose=1)
mcp = ModelCheckpoint(monitor='loss',filepath='pesos.h5',save_best_only=True, verbose = 1)

redeNeural.fit(previsores, preco,  epochs=100, batch_size=32, callbacks=[stopping, rlr, mcp])

base_teste = pd.read_csv('petr4_teste.csv')
preco_real_teste = base_teste.iloc[:, 1:2].values
frames = [base, base_teste]
base_completa = pd.concat(frames)
base_completa = base_completa.drop('Date', axis = 1)

entradas = base_completa[len(base_completa) - len(base_teste) - 90:].values
entradas = normalizador.transform(entradas)

X_teste = []
for i in range(90, 112):
    X_teste.append(entradas[i-90:i, 0:6])
X_teste = np.array(X_teste)
previsoes = redeNeural.predict(X_teste)
previsoes = normalizador_previsao.inverse_transform(previsoes)

previsoes.mean()
preco_real_teste.mean()
    
plt.plot(preco_real_teste, color = 'red', label = 'Preço real')
plt.plot(previsoes, color = 'blue', label = 'Previsões')
plt.title('Previsão preço das ações')
plt.xlabel('Tempo')
plt.ylabel('Valor Yahoo')
plt.legend()
plt.show()