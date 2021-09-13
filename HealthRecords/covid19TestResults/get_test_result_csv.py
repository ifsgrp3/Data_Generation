import pandas as pd
import glob
import csv

path = r'/Users/michelle/PycharmProjects/ifs4205_database/covid19_test_results'
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename)
    li.append(df)

frame = pd.concat(li, axis=1)
frame.to_csv("covid19_test_results.csv", index=False)

