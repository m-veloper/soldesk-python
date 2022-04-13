import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(500, 1000, size=(100, 4)), columns=[2015, 2016, 2017, 2018])
print(df)

df = pd.DataFrame(np.random.rand(100, 4), columns=[2015, 2016, 2017, 2017])
print(df)

# 엑셀 쓰기
df.to_excel('data/result_s4.xlsx', index=False, header=True)
print('commit')
