import numpy as np, pandas as pd, os
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

for player in os.listdir('./Players/.'):
    dataset = pd.read_csv('./Players/' + player)
    X = dataset.Seasons.values.reshape(-1, 1)
    y = dataset.Points.values.reshape(-1, 1)
    
    # Feature Scaling
    sc_X = StandardScaler()
    sc_y = StandardScaler()
    X = sc_X.fit_transform(X)
    y = sc_y.fit_transform(y)

    # Fitting SVR to the dataset
    regressor = SVR(kernel = 'rbf')
    regressor.fit(X, y.ravel())

    # Calculate the Score 
    score = regressor.score(X, y)  
    # Print the Score
    print(player, 100 * score)
    import warnings
    warnings.filterwarnings('ignore')

    # Save the trained model as a pickle string. 
    import joblib
    joblib.dump(regressor, './Regressors/' + player[:-4] + '.pkl')
    joblib.dump(sc_X, './Regressors/' + player[:-4] + 'Scaler_X.pkl')
    joblib.dump(sc_y, './Regressors/' + player[:-4] + 'Scaler_y.pkl')

