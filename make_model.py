import numpy as np, pandas as pd
datasetMatches = pd.read_csv("Modified_Matches.csv")
datasetMatches = datasetMatches.iloc[:,1:]
# datasetMatches.head()
y = datasetMatches.iloc[:, -1].values
X = datasetMatches.iloc[:, 2:9].values

# Encoding The Categorical Variables
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
labelEncoderX1 = LabelEncoder()       # For encoding teams
X[:, 0] = labelEncoderX1.fit_transform(X[:, 0])
X[:, 1] = labelEncoderX1.transform(X[:, 1])

labelEncoderX2 = LabelEncoder()        # for encoding toss winner
X[:, 2] = labelEncoderX2.fit_transform(X[:, 2])

labelEncoderX3 = LabelEncoder()        # for encoding toss results
X[:, 3] = labelEncoderX3.fit_transform(X[:, 3])

labelEncoderX4 = LabelEncoder()         #for encoding stadium name
X[:, 4] = labelEncoderX4.fit_transform(X[:, 4])

labelEncoder_Y = LabelEncoder()         #for encoding winner 
y = labelEncoder_Y.fit_transform(y)

ct = ColumnTransformer([('one_hot_encoder', OneHotEncoder(categories='auto'), [0])],remainder='passthrough')
X = ct.fit_transform(X)
X = X[:, 1:]

ct1 = ColumnTransformer([('one_hot_encoder', OneHotEncoder(categories='auto'), [12])],remainder='passthrough')
X = ct1.fit_transform(X)
X = X[:,1:]

ct2 = ColumnTransformer([('one_hot_encoder', OneHotEncoder(categories='auto'), [26])],remainder='passthrough')
X = ct2.fit_transform(X)
X = X[:,1:]

from sklearn.model_selection import train_test_split
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.2, random_state=0)

import keras
from keras.models import Sequential    #### for initializing the Neural Network.
from keras.layers import Dense         #### for adding diffrent layers.
from keras.layers import Dropout

def create_model(init_mode='uniform', activation = 'relu', neurons = 10):
    # define model
    model = Sequential()
    model.add(Dense(neurons, kernel_initializer=init_mode, activation=activation, input_dim=60)) 
#     model.add(Dropout(0.1))
    model.add(Dense(neurons, kernel_initializer=init_mode, activation=activation))
    model.add(Dense(neurons, kernel_initializer=init_mode, activation = activation))
    model.add(Dense(neurons, kernel_initializer=init_mode, activation = activation))
    model.add(Dense(1, kernel_initializer=init_mode, activation='sigmoid'))
    # compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

from sklearn.model_selection import GridSearchCV
from keras.wrappers.scikit_learn import KerasClassifier
model_CV = KerasClassifier(build_fn=create_model, epochs=80, batch_size=10, verbose=1)

model_CV.fit(XTrain,yTrain)

yPred = model_CV.predict(XTest)
# yPred = (yPred > 0.5)

from sklearn import metrics
print(metrics.accuracy_score(yTest, yPred))

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(yTest, yPred)
print(cm)

import joblib
joblib.dump(model_CV, './model/model.pkl')
joblib.dump(labelEncoderX1, './model/encoder1.pkl')
joblib.dump(labelEncoderX2, './model/encoder2.pkl')
joblib.dump(labelEncoderX3, './model/encoder3.pkl')
joblib.dump(labelEncoderX4, './model/encoder4.pkl')

joblib.dump(ct, './model/column_T.pkl')
joblib.dump(ct1, './model/column_T1.pkl')
joblib.dump(ct2, './model/column_T2.pkl')