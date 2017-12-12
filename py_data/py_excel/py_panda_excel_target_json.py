import pandas as pd
import numpy as np

# Assign spreadsheet filename to `file`
file = 'test.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

print xl.sheet_names

df1 = xl.parse('Sheet2', header=0, parse_cols="E:F")
df1 = df1.replace(np.nan, '', regex=True)

print df1

dic = {}

for i in df1.index:
    dic[df1.at[i,'Unnamed: 0']] = df1.at[i,'Unnamed: 1']
print dic

df2 = xl.parse('Sheet2', header=None, skiprows=3, parse_cols="J:N")
df2 = df2.replace(np.nan, '', regex=True)
print df2
print df2.columns 
cols = []
rows = []
for i in df2.index:
    _row = []
    for j in df2.columns:
        if df2.at[i,j]:
            _row.append(df2.at[i,j])
    if len(cols) == 0:
        cols += _row
    else:
        rows.append(_row)

json = []
for row in rows:
    _row = {}
    for index,col in enumerate(cols):
        _row[col] = row[index]
    json.append(_row)

print json

