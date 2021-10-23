import pandas as pd
import time 

chunksize = 10 ** 6
# chunksize = 100
print(chunksize)

writer = pd.ExcelWriter('/Users/eason/Downloads/a/a.xlsx', engine='openpyxl')
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
for idx, chunk in enumerate(pd.read_csv('/Users/eason/Downloads/a/a.csv', chunksize=chunksize)):
    print(chunk)
    # chunk.to_excel('/Users/eason/Downloads/a_'+str(idx)+'.xlsx')  单独这么写不需要用writer
    chunk.to_excel(excel_writer=writer, sheet_name=str(idx), encoding="GBK")

writer.save()
writer.close()
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("FINISH")