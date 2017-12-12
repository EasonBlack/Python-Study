import pandas as pd
import numpy as np
import json
import sys
import os

mytxt = open('content.txt', 'w')

print 'Input File Path: ',
file = raw_input()

print '1 Tabel'
print '2 Json'
print 'Select Data Type:',
datatype = raw_input()

xl = pd.ExcelFile(file)
for index,sheet_name in enumerate(xl.sheet_names):
    print index, sheet_name

print 'selected Sheet Index: ',
sheetIndex = raw_input()

print 'Skip Rows',
skipRows = raw_input()
skipRows = skipRows or 0

if int(sheetIndex) > len(xl.sheet_names) :
    print 'Please check the sheet index, out of range'
    sys.exit()

print 'selected Columns: ',
cols = raw_input()

df1 = xl.parse(int(sheetIndex),  header=None, skiprows=int(skipRows), parse_cols=cols)
df1 = df1.replace(np.nan, '', regex=True)

print df1

if datatype == '2':
    mytxt.write('{\r\n')
    for i in df1.index:
        mytxt.write("\t\'{0}\':\'{1}\', \r\n".format( df1.at[i,0], str(df1.at[i,1])))
    mytxt.write('}')
elif datatype == '1':
    cols = []
    rows = []
    for i in df1.index:
        _row = []
        for j in df1.columns:
            if df1.at[i,j]:
                _row.append(df1.at[i,j])
        if len(cols) == 0:
            cols += _row
        else:
            rows.append(_row)
    
    table = []
    for row in rows:
        _row = {}
        for index,col in enumerate(cols):
            _row[col] = row[index]
        table.append(_row)
    print  json.dumps(table)
    
    mytxt.write('[\r\n')
    for row in table:
        mytxt.write("\t{0}, \r\n".format(json.dumps(row)))
    mytxt.write(']')

mytxt.close()

os.system("notepad.exe content.txt")
