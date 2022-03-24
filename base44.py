import pandas as pd

# 계절별 서울/부산 지역 온도 데이터 정의
temperatures = [[3.3, 34.5, 14.2, -10], [7.1, 32.1, 10.7, 2]]
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
regions = ['Seoul', 'Pusan']

# 데이터 프레임
data = pd.DataFrame(temperatures, index=regions, columns=seasons)

# 출력
print(data)
print('=' * 50)
print(data.index)
print(data.columns)
print(data.values)
print('=' * 50)
