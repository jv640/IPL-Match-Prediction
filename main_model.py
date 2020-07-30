import pandas as pd, joblib
from ast import literal_eval

matches_data = pd.read_csv('Matches.csv')
playing_11_data = pd.read_csv('playing_11.csv')

rows = matches_data.shape[0]

for i in range(0, 3):
    match_id = matches_data['ID']

    ########        HOME WEIGHT         #####################
    home_weight = 0
    home_players = playing_11_data["Team_2"][i]
    home_players = literal_eval(home_players)
    for player in home_players:
        player = " ".join(player.split()) + ".csv"
        player = player.replace(" ", "_")
        player_data = pd.read_csv('./Players/' + player)
        player_points = player_data[player_data["Seasons"] == 2020]
        if player_points.empty == False:
            player_points = player_points["Points"]
            player_points = pd.to_numeric(player_points)
        else:
            loaded_regressor = joblib.load('./Regressors/' + player[ : -4] + '.pkl')
            player_points = loaded_regressor.predict(matches_data["Season"][i].reshape(-1, 1))
            player_points = sc_y.inverse_transform(player_points)
        home_weight = home_weight + player_points
        del player_points, player_data

    print(home_weight)
    # matches_data["Home_points"][i] = home_weight/11

    ########        AWAY WEIGHT         #####################

#     away_weight = 0
#     away_players = playing_11_data["Team_1"][i]
#     away_players = literal_eval(away_players)
#     for player in away_players:
#         player = " ".join(player.split()) + ".csv"
#         player = player.replace(" ", "_")
#         player_data = pd.read_csv('./Players/' + player)
#         player_points = player_data[player_data["Seasons"] == matches_data['Season'][i]]
#         player_points = player_points["Points"]
#         player_points = pd.to_numeric(player_points)
#         away_weight = away_weight + player_points
#         del player_points, player_data
#     # print(type(away_weight))
#     matches_data["Away_points"][i] = away_weight/11

# df = pd.DataFrame(matches_data)
# df.to_csv('Modified_Matches.csv')

    