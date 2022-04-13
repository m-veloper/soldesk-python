from pandas import Series

# Series
series1 = Series([92600, 92400, 92100, 92300])
print(series1)

print('count : ', series1.count())

# 요약
print('describe : ', series1.describe())

# 인덱스
print(series1[0])

# index 선언
series1 = Series([92600, 92400, 92100, 92300],
                 index=['2021-05-10', '2021-05-11', '2021-05-12', '2021-05-13'])
print(series1)
print(series1.index)
print(series1.values)

# 조회
for data in series1.index:
    print('data : ', data)

for price in series1.values:
    print('price : ', price)

# Series 선언
series_g1 = Series([10, 20, 30], index=['n1', 'n2', 'n3'])
series_g2 = Series([10, 30, 20], index=['n1', 'n2', 'n3'])

# Series 병합
sum = series_g1 + series_g2
mul = series_g1 * series_g2
cul = (series_g1 * series_g2) * 0.5

print("=========sum=========")
print(sum)
print("=========mul=========")
print(mul)
print("=========cul=========")
print(cul)
