import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV


import keras


previsores = pd.read_csv("entradas_breast.csv")
classes = pd.read_csv("saidas_breast.csv")

def criarRede():
    redeNeural = Sequential()
    redeNeural.add(Dense(units=16, activation='relu', kernel_initializer='random_uniform', input_dim=30))
    #   As entradas não definidas como 0 são aumentadas em 1 / (1 - taxa) 
    #   de forma que a soma de todas as entradas permaneça inalterada.
    redeNeural.add(Dropout(0.2))
    redeNeural.add(Dense(units=1, activation='sigmoid'))
    #optimizador = keras.optimizers.Adam(lr=0.001, decay=0.001, clipvalue=0.5)
    redeNeural.compile(optimizer='Adam', loss='binary_crossentropy', metrics=['binary_accuracy'])
    return redeNeural

classificador = KerasClassifier(build_fn=criarRede, batch_size=10, epochs=100)

resultados = cross_val_score(estimator=classificador, X=previsores, y=classes, cv=30, scoring='accuracy')
 
media = resultados.mean()
desvio = resultados.std()
