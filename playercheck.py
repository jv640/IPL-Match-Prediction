import pandas as pd, os
from ast import literal_eval
not_found = set()
for files in os.listdir('./Players/.'):
    found = False
    players = open("all_players.txt", "r")
    for line in players:
        line = line.rstrip("\n")
        # print(len(line), line)
        # print(len(files), files)
        if files == line:
            found = True
            break
    players.close()
    if found == False:
        not_found.add(files)

print(not_found)
print(len(not_found))