import csv
import random, sys
import pandas as pd
import string

data = pd.read_csv("/Users/michelle/PycharmProjects/ifs4205_database/covid19_test_results/covid19_test_results.csv", sep=',',
                   names=['nric', 'covid19_test_type', 'test_result'])
p = 0
sys.stdout = open("load_covid19_test_results.sql", "w")
for i in range(5000):
    print("CALL add_covid19_results('" + str(data['nric'].iloc[p]) + "', '" + str(data['covid19_test_type'].iloc[p]) +
          "', '" + str(data['test_result'].iloc[p]) + "');")

    p += 1
sys.stdout.close()
