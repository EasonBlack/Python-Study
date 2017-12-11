import pandas as pd
import os

mytxt = open('content.txt', 'w')

file = 'test.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

print 'selected cols: ',
cols = raw_input()

print xl.sheet_names

df1 = xl.parse('Sheet2',  parse_cols=cols)

print df1

dic = {}

mytxt.write('{\r\n')
for i in df1.index:
    mytxt.write('\t' + df1.at[i,'Unnamed: 0'] + ': \'' + str(df1.at[i,'Unnamed: 1']) + '\',\r\n')
    dic[df1.at[i,'Unnamed: 0']] = df1.at[i,'Unnamed: 1']
mytxt.write('}')

mytxt.close()
os.system("notepad.exe content.txt")