import joblib

model = joblib.load('./model/model.pkl')
en1 = joblib.load('./model/encoder1.pkl')
en2 = joblib.load('./model/encoder2.pkl')
en3 = joblib.load('./model/encoder3.pkl')
en4 = joblib.load('./model/encoder4.pkl')
en5 = joblib.load('./model/encoder5.pkl')

ct = joblib.load('./model/column_T.pkl')
ct1 = joblib.load('./model/column_T1.pkl')
ct2 = joblib.load('./model/column_T2.pkl')

X = [home, away, tossWin, tossDec, venue, home_players, away_players]

for player in home_players:
    player = " ".join(player.split()) + ".csv"
    player = player.replace(" ", "_")
    if os.path.isfile('./Players/' + player) == False:
        continue
    player_data = pd.read_csv('./Players/' + player)
    player_points = player_data[player_data["Seasons"] == 2020]
    if player_points.empty == False:
        player_points = player_points["Points"]
        if np.isfinite(player_points.any()) == False:
            continue
        player_points = player_points.apply(lambda x: float(x))
        home_weight = home_weight + player_points
    else:
        loaded_regressor = joblib.load('./Regressors/' + player[ : -4] + '.pkl')
        sc_X = joblib.load('./Regressors/' + player[ : -4] + 'Scaler_X.pkl')
        player_points = loaded_regressor.predict(sc_X.transform(matches_data["Season"][i].reshape(-1, 1)))
        sc_y = joblib.load('./Regressors/' + player[ : -4] + 'Scaler_y.pkl')
        player_points = sc_y.inverse_transform(player_points)
        home_weight = home_weight + player_points
    del player_points, player_data
    home_weight = home_weight[np.logical_not(np.isnan(home_weight))]
    if isinstance(home_weight, np.ndarray) == False:
        if home_weight.dropna().empty:
            continue
    # print(home_weight)
    home_weight = home_weight.astype(int)
    X.append(home_weight)

for player in away_player:
    player = " ".join(player.split()) + ".csv"
    player = player.replace(" ", "_")
    if os.path.isfile('./Players/' + player) == False:
        continue
    player_data = pd.read_csv('./Players/' + player)
    player_points = player_data[player_data["Seasons"] == 2020]
    if player_points.empty == False:
        player_points = player_points["Points"]
        if np.isfinite(player_points.any()) == False:
            continue
        player_points = player_points.apply(lambda x: float(x))
        away_weight = away_weight + player_points
    else:
        loaded_regressor = joblib.load('./Regressors/' + player[ : -4] + '.pkl')
        sc_X = joblib.load('./Regressors/' + player[ : -4] + 'Scaler_X.pkl')
        player_points = loaded_regressor.predict(sc_X.transform(matches_data["Season"][i].reshape(-1, 1)))
        sc_y = joblib.load('./Regressors/' + player[ : -4] + 'Scaler_y.pkl')
        player_points = sc_y.inverse_transform(player_points)
        away_weight = away_weight + player_points
    del player_points, player_data
    away_weight = away_weight[np.logical_not(np.isnan(away_weight))]
    if isinstance(away_weight, np.ndarray) == False:
        if away_weight.dropna().empty:
            continue
    # print(away_weight)
    away_weight = away_weight.astype(int)
    X.append(away_weight)

X[:, 0] = labelEncoderX1.transform(X[:, 0])
X[:, 1] = labelEncoderX1.transform(X[:, 1])
X[:, 2] = labelEncoderX2.transform(X[:, 2])
X[:, 3] = labelEncoderX3.transform(X[:, 3])
X[:, 4] = labelEncoderX4.transform(X[:, 4])

X = ct.transform(X)
X = X[:, 1:]
X = ct1.transform(X)
X = X[:, 1:]
X = c2t.transform(X)
X = X[:, 1:]

yPred = model.predict(X)

ypred = en5.inverse_transform(yPred)

