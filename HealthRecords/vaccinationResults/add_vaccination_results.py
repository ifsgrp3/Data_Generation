import csv
import random, sys
import pandas as pd
import string

data = pd.read_csv("/Users/michelle/PycharmProjects/ifs4205_database/vaccination_results/vaccination_results.csv", sep=',',
                   names=['nric', 'vaccination_status', 'vaccine_type', 'vaccination_centre_location', 'first_dose_date',
                          'second_dose_date'])
p = 0
sys.stdout = open("load_vaccination_results.sql", "w")
for i in range(5000):
    print("CALL add_vaccination_results('" + str(data['nric'].iloc[p]) + "', '" + str(data['vaccination_status'].iloc[p])
          + "', '" + str(data['vaccine_type'].iloc[p]) + "', '" + str(data['vaccination_centre_location'].iloc[p]) + "', '" +
          str(data['first_dose_date'].iloc[p]) + "', '" + str(data['second_dose_date'].iloc[p]) + "');")
    p += 1
sys.stdout.close()
