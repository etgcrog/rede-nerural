import pandas as pd
from sklearn.model_selection import train_test_split

entradas = pd.read_csv("entradas_breast.csv")
saidas = pd.read_csv("saidas_breast.csv")

####################################################
########TREINAMENTO TREINAMENTO TREINAMENTO#########
####################################################

treinamento, teste, cl_treinamento, cl_teste = train_test_split(entradas, saidas, test_size=0.25)

from keras.models import Sequential
from keras.layers import Dense

redeNeural = Sequential()
redeNeural.add(Dense(units=16, activation='relu', kernel_initializer='random_uniform', input_dim=30))
redeNeural.add(Dense(units=16, activation='relu', kernel_initializer='random_uniform'))
redeNeural.add(Dense(units=16, activation='relu', kernel_initializer='random_uniform'))
redeNeural.add(Dense(units=16, activation='relu', kernel_initializer='random_uniform'))
redeNeural.add(Dense(units=16, activation='relu', kernel_initializer='random_uniform'))
redeNeural.add(Dense(units=1, activation='sigmoid'))

#optimizador = keras.optimizers.Adam(lr=0.001, decay=0.001, clipvalue=0.5)

redeNeural.compile(optimizer='Adam', loss='binary_crossentropy', metrics=['binary_accuracy'])
#fit com os previsores e épocas, treinamento real!!!
redeNeural.fit(treinamento, cl_treinamento, batch_size=10, epochs=100)


###################################################
##########TESTES  TESTES   TESTES##################
###################################################

from sklearn.metrics import confusion_matrix, accuracy_score

peso0 = redeNeural.layers[0].get_weights()
print(peso0)

previsoes = redeNeural.predict(teste)
previsoes = (previsoes > 0.5)

resultados = accuracy_score(cl_teste, previsoes)
resultados_matriz=confusion_matrix(cl_teste, previsoes)

#resultados = redeNeural.evaluate(teste, cl_teste)

