import pandas as pd

# Assign spreadsheet filename to `file`
file = 'test.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

print xl.sheet_names

df1 = xl.parse('Sheet2', header=1, parse_cols="E:F")

print df1

dic = {}

for i in df1.index:
    dic[df1.at[i,'Unnamed: 0']] = df1.at[i,'Unnamed: 1']
    # print  df1.at[i,'Unnamed: 0'], df1.at[i,'Unnamed: 1']

print dic