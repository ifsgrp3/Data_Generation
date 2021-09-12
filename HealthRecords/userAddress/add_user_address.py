import csv
import random, sys
import pandas as pd
import string

data = pd.read_csv("/Users/michelle/PycharmProjects/ifs4205_database/user_address/user_address.csv", sep=',',
                   names=["street_name", "nric", "area", "zip_code", "unit_number"])
p = 0
sys.stdout = open("load_user_address.sql", "w")
for i in range(5000):
    print("CALL add_user_address('" + str(data['nric'].iloc[p]) + "', '" + str(data['street_name'].iloc[p]) + "', '"
          + str(data['unit_number'].iloc[p]) + "', '" + str(data['zip_code'].iloc[p]) + "', '" + str(data['area'].iloc[p]) + "');")

    p += 1
sys.stdout.close()

