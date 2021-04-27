import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils  #DUMMY


base = pd.read_csv('iris.csv')
previsores = base.iloc[:, 0:4].values
classe = base.iloc[:, 4].values
    
from sklearn.preprocessing import LabelEncoder

labelenconder = LabelEncoder()
classe = labelenconder.fit_transform(classe)
classe_dummy = np_utils.to_categorical(classe)

from sklearn.model_selection import train_test_split

prev_train, prev_test, cls_train, cls_test = train_test_split(previsores, classe_dummy)

redeNeural = Sequential()
redeNeural.add(Dense(units = 4, activation='relu', input_dim = 4))
redeNeural.add(Dense(units = 4, activation='relu'))
redeNeural.add(Dense(units = 3, activation='softmax'))
redeNeural.compile(optimizer = 'adam', loss='categorical_crossentropy',
                   metrics=['categorical_accuracy'])
redeNeural.fit(prev_train, cls_train, batch_size=10, epochs=1000)

resultado = redeNeural.evaluate(prev_test, cls_test)

prev_futures = redeNeural.predict(prev_test)
prev_futures = prev_futures > 0.5
import numpy as np
cls_test2 = [np.argmax(n) for n in cls_test]
prev_futures2 = [np.argmax(n) for n in prev_futures]


from sklearn.metrics import confusion_matrix
matrix = confusion_matrix(prev_futures2, cls_test2)




