import pandas as pd
import numpy as np

# Assign spreadsheet filename to `file`
file = 'test.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

print xl.sheet_names

df1 = xl.parse('Sheet2', header=None, parse_cols="E:F")
df1 = df1.replace(np.nan, '', regex=True)

print df1

dic = {}

for i in df1.index:
    dic[df1.at[i,0]] = df1.at[i,1]

print dic