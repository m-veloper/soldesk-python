import pandas as pd

# 시리즈 객체
numbers = pd.Series([100, 200, 300])
print(numbers)

# 인덱스 지정
score = pd.Series([90, 64, 87], index=['백설', '재원', '경철'])
print(score)
print(score.index)
print(score.values)
print(score.index[1], score.values[1])
