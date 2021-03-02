import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.wrappers.scikit_learn import KerasClassifier

from sklearn.model_selection import GridSearchCV


previsores = pd.read_csv('entradas_breast.csv')
classes = pd.read_csv('saidas_breast.csv')

def criarRedeNeural(optimizador, loos, initializer, neurons, ativacao):
    redeNeural = Sequential()
    redeNeural.add(Dense(units=neurons, activation=ativacao, kernel_initializer=initializer,input_dim=30))
    redeNeural.add(Dropout(0.2))
    redeNeural.add(Dense(units=neurons, activation=ativacao, kernel_initializer=initializer))
    redeNeural.add(Dense(units=1, activation='sigmoid'))
    
    redeNeural.compile(optimizer=optimizador, loss=loos, metrics = ['binary_accuracy'])
    
    return redeNeural

classificador = KerasClassifier(build_fn = criarRedeNeural)

parametros = {'batch_size' : [10,30],
              'epochs' : [100,200],
              'optimizador' : ['adam', 'sgd'],
              'loos' : ['binary_crossentropy', 'hinge'],
              'initializer' : ['random_uniform', 'normal'],
              'ativacao' : ['relu', 'tanh'],
              'neurons' : [16,8]}

grid_search = GridSearchCV(estimator = classificador, param_grid=parametros, scoring='accuracy',cv=10)
grid_search = grid_search.fit(previsores, classes)

best = grid_search.best_params_
best_score = grid_search.best_score_

