import pandas as pd, os
from ast import literal_eval

playing_11 = pd.read_csv('playing_11.csv')
rows = playing_11.shape[0]
counter = 0
not_found = set()
players = set()
for i in range(0, rows):
    player_list = playing_11["Team_1"][i]
    player_list = literal_eval(player_list)
    # print(type(player_list))
    for player in player_list:
        player = player.strip()
        player = player.replace(" ", "_")
        name =  player + ".csv"
        players.add(name)
        if os.path.isfile('./Players/' + name):
            print("exist")
        else:
            print("not exist")
            counter = counter + 1
            not_found.add(name)
    
    player_list = playing_11["Team_2"][i]
    player_list = literal_eval(player_list)
    # print(type(player_list))
    for player in player_list:
        player = player.strip()
        player = player.replace(" ", "_")
        name =  player + ".csv"
        players.add(name)
        if os.path.isfile('./Players/' + name):
            print("exist")
        else:
            print("not exist")
            counter = counter + 1
            not_found.add(name)

print(not_found)
print(counter)
with open('not_found.txt', 'w') as f:
    for item in not_found:
        f.write("%s\n" % item)
with open('all_players.txt', 'w') as f:
    for item in players:
        f.write("%s\n" % item)

