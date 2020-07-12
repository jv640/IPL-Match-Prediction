import pandas as pd
import os
from csv import writer

dataset = pd.read_csv("All_Year_Player_Points_IPL.csv")
rows = dataset.shape[0]
# players = {}
# print(rows)
for i in range(0, rows):
    name = " ".join(dataset["PLAYER"][i].split()) + ".csv"
    name = name.replace(" ", "_")
    # print(name)
    data = [dataset["Year"][i], dataset["Pts"][i]]
    if os.path.isfile(name):
        ff = open(name, "a", newline="")
        csv_writer = writer(ff)
        csv_writer.writerow(data)
        ff.close()
    else:
        ff = open(name, "a", newline="")
        row = ['Seasons', 'Points']
        csv_writer = writer(ff)
        csv_writer.writerow(row)
        csv_writer.writerow(data)
        ff.close()


        
    

