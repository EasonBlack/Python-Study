import pandas as pd

# Assign spreadsheet filename to `file`
file = 'test.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

print xl.sheet_names

df1 = xl.parse('Sheet1')

for i in df1.index:
    print df1['name'][i] , df1['num'][i]

