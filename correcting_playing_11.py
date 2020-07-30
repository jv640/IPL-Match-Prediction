import pandas as pd
from ast import literal_eval

stadiums = pd.read_csv('Stadium_and_Home_Teams.csv')
playing_11_data = pd.read_csv('playing_11.csv')

matches = pd.read_csv('Matches_prev.csv')
rows = matches.shape[0]

for i in range(0, rows):
    found = False
    home_teams = stadiums[stadiums["Stadium"] == matches["Venue"][i]]

    for home_team in home_teams["HomeTeams_short"]:
        home_team_list = literal_eval(home_team)
        for team in home_team_list:
            if  matches["Home"][i] == team:
                # print("not")
                found = True

    if found == False:
        swap = matches["Home"][i]
        matches["Home"][i] = matches["Away"][i]
        matches["Away"][i] = swap

        if matches["TossWin"][i] == "Away":
            matches["TossWin"][i] = "Home"
        elif matches["TossWin"][i] == "Home":
            matches["TossWin"][i] = "Away"
        if matches["Winner"][i] == "Away":
            matches["Winner"][i] = "Home"
        elif matches["Winner"][i] == "Home":
            matches["Winner"][i] = "Away"
        print("changed")
        swap_players = playing_11_data["Team_1"][i]
        playing_11_data["Team_1"][i] = playing_11_data["Team_2"][i]
        playing_11_data["Team_2"][i] = swap_players

df = pd.DataFrame(playing_11_data)
df.to_csv('Modified_Playing_11.csv')