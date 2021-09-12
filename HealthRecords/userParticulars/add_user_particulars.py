import csv
import random, sys
import pandas as pd
import string

data = pd.read_csv("/Users/michelle/PycharmProjects/ifs4205_database/user_particulars/user_particulars.csv", sep=',',
                   names=["contact_number", "first_name", "age", "gender", "date_of_birth", "nric", "last_name", "race"])
p = 0
sys.stdout = open("load_user_particulars.sql", "w")
for i in range(5000):
    print("CALL add_user_particulars('" + str(data['nric'].iloc[p]) + "', '" + str(data['first_name'].iloc[p]) +
          "', '" + str(data['last_name'].iloc[p]) + "', '" + str(data['date_of_birth'].iloc[p]) + "', '" + str(data['age'].iloc[p]) +
          "', '" + str(data['gender'].iloc[p]) + "', '" + str(data['race'].iloc[p]) + "', '" + str(data['contact_number'].iloc[p]) + "');")
    p += 1
sys.stdout.close()

