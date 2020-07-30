import pandas as pd

matches_data = pd.read_csv('Matches.csv')
playing_11_data = pd.read_csv('playing_11.csv')

rows = matches_data.shape[0]

for i in range(0, 3):
    match_id = matches_data['ID']
    