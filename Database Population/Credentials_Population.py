import csv
import random, sys
import pandas as pd
import string

data = pd.read_csv('Final_Credentials_Data.csv', sep=',',
                   names=["NRIC","password", "hashed_password", "user_salt", "ble", "account_role", "admin_id"])
p = 0
sys.stdout = open("load_credentials.sql", "w")
for i in range(5000):
    print("CALL add_user('" + data['NRIC'].iloc[p] + "', '" + data['hashed_password'].iloc[p]
          + "', '" + data['user_salt'].iloc[p] + "', '" + str(data['ble'].iloc[p]) + "', '" +
          str(data['account_role'].iloc[p]) + "', '" + str(data['admin_id'].iloc[p]) + "');" )
    p+= 1
sys.stdout.close()
