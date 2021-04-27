import pandas as pd
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.model_selection import cross_val_score
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV


base = pd.read_csv('iris.csv')
previsores = base.iloc[:, 0:4].values
classe = base.iloc[:, 4].values

from sklearn.preprocessing import LabelEncoder

labelencoder = LabelEncoder()
classe = labelencoder.fit_transform(classe)
classe_dummy = np_utils.to_categorical(classe)


def criarRede(optimizer, drop, activation, neurons):
    redeNeural = Sequential()
    redeNeural.add(Dense(neurons, activation, input_dim=4))
    redeNeural.add(Dropout(drop))
    redeNeural.add(Dense(neurons, activation))
    redeNeural.add(Dense(neurons, 'softmax'))
    redeNeural.compile(optimizer=optimizer, 
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
    return redeNeural


classificador = KerasClassifier(build_fn=criarRede)

parametros = {'batch_size': [10, 15, 25],
              'epochs': [100, 250, 500],
              'optimizer': ['adam', 'Adamax'],
              'drop': [0.2, 0.25, 0.3],
              'activation': ['relu', 'elu'],
              'neurons': [4, 6, 8]}

grid_search = GridSearchCV(estimator=classificador,
                           param_grid=parametros,
                           cv=10)

grid_search = grid_search.fit(previsores, classe)
melhores_parametros = grid_search.best_params_
melhor_precisao = grid_search.best_score_



    
    