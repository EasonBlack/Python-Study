import pandas as pd
import numpy as np
import sys
import os

mytxt = open('content.txt', 'w')

print 'Input File Path: ',
file = raw_input()

xl = pd.ExcelFile(file)
for index,sheet_name in enumerate(xl.sheet_names):
    print index, sheet_name

print 'selected Sheet Index: ',
sheetIndex = raw_input()

if int(sheetIndex) > len(xl.sheet_names) :
    print 'Please check the sheet index, out of range'
    sys.exit()

print 'selected Columns: ',
cols = raw_input()

df1 = xl.parse(int(sheetIndex),  header=None,  parse_cols=cols)
df1 = df1.replace(np.nan, '', regex=True)

print df1

mytxt.write('{\r\n')
for i in df1.index:
    mytxt.write("\t\'{0}\':\'{1}\', \r\n".format( df1.at[i,0], str(df1.at[i,1])))
mytxt.write('}')
mytxt.close()

os.system("notepad.exe content.txt")
