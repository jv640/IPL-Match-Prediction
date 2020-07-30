import pandas as pd, joblib, os, math, numpy as np
from ast import literal_eval

matches_data = pd.read_csv('Matches.csv')
playing_11_data = pd.read_csv('playing_11.csv')

rows = matches_data.shape[0]

for i in range(0, rows):
    match_id = matches_data['ID']

    ########        HOME WEIGHT         #####################
    home_weight = 0

    home_players = playing_11_data["Team_2"][i]
    home_players = literal_eval(home_players)
    for player in home_players:
        player = " ".join(player.split()) + ".csv"
        player = player.replace(" ", "_")
        if os.path.isfile('./Players/' + player) == False:
            continue
        player_data = pd.read_csv('./Players/' + player)
        player_points = player_data[player_data["Seasons"] == matches_data['Season'][i]]
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
        matches_data["Home_points"][i] = home_weight


    #######        AWAY WEIGHT         #####################

    away_weight = 0
    away_players = playing_11_data["Team_1"][i]
    away_players = literal_eval(away_players)
    for player in away_players:
        player = " ".join(player.split()) + ".csv"
        player = player.replace(" ", "_")
        if os.path.isfile('./Players/' + player) == False:
            continue
        player_data = pd.read_csv('./Players/' + player)
        player_points = player_data[player_data["Seasons"] == matches_data['Season'][i]]
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
        away_weight = away_weight.astype(int)
        matches_data["Away_points"][i] = away_weight

    del home_weight, home_players, away_weight, away_players
    print(int(i+1)/rows)

df = pd.DataFrame(matches_data)
df.to_csv('Modified_Matches.csv')

    