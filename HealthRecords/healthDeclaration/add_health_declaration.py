import csv
import random, sys
import pandas as pd
import string

data = pd.read_csv("/Users/michelle/PycharmProjects/ifs4205_database/health_declaration/health_declaration.csv", sep=',',
                   names=["covid_symptoms", "nric", "temperature"])
p = 0
sys.stdout = open("load_health_declaration.sql", "w")
for i in range(5000):
    print("CALL add_health_declaration('" + str(data['nric'].iloc[p]) + "', '" + str(data['covid_symptoms'].iloc[p]) +
          "', '" + str(data['temperature'].iloc[p]) + "');")

    p += 1
sys.stdout.close()

