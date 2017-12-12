import pandas as pd
import numpy as np
import sys
import os

mytxt = open('content.txt', 'w')

file = 'test.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

print 'selected Sheet: '
sheet = raw_input()

print xl.sheet_names
selectedSheet = ''
for sheet_name in xl.sheet_names:
    if sheet.strip() == sheet_name.strip():
        selectedSheet = sheet_name
        break

if selectedSheet == '' :
    print 'Please check the sheet name, not exist in excel!'
    sys.exit()

print 'selected Columns: '
cols = raw_input()


print xl.sheet_names
print selectedSheet

df1 = xl.parse(selectedSheet, header=None,  parse_cols=cols)
df1 = df1.replace(np.nan, '', regex=True)

print df1

dic = {}

mytxt.write('{\r\n')
for i in df1.index:
    mytxt.write("\t\'{0}\':\'{1}\', \r\n".format( df1.at[i,0], str(df1.at[i,1])))
mytxt.write('}')

mytxt.close()
os.system("notepad.exe content.txt")