import csv
import random, sys
import pandas as pd


data1 = pd.read_csv('NEWNRIC.csv')
data2 = pd.read_csv('password_with_hash1.csv')
df3 = pd.concat([data1, data2], axis=1)
df3.to_csv('NRIC_PASSWORD.csv', index=False)

