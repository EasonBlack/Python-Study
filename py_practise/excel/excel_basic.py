import pandas as pd
import numpy as np
df = pd.read_excel("demo.xlsx", 'Sheet2')
print df.keys()
dt = df.sort_values(['team'])#[['name','team']] 
dt = dt.query("team==1").head()
#dt = dt.where(dt['team'] == 2).drop_duplicates(['name','team'])
dt = dt.append(dt.count(), ignore_index=True)
print dt
