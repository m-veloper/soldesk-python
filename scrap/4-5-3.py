import pandas as pd
import numpy as np

# 램덤으로 DataFrame 생성
# df=pd.DataFrame(np.random.randint(0, 100, size=(100,4)), columns=list('ABCD') )
# df=pd.DataFrame(np.random.randn(100, 4), columns=list('ABCD') ) #randn:음수값 출력
df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=['ONE', 'TWO', 'THREE', 'FOUR'])
print(df)

# CSV로 저장
df.to_csv("data/result2.csv", index=False)
print('commit')
