import pandas as pd
import csv

# 기본 읽기
# df=pd.read_csv('data/csv_s1.csv')
# print(df)

# 행 스킵, 0행 인식하지 않음
# df=pd.read_csv('data/csv_s1.csv', skiprows=[0])
# print(df)

# 행 스킵, 0행 인식하지 않음, Header생략
# df=pd.read_csv('data/csv_s1.csv', skiprows=[0], header=None)
# print(df)

# 행 스킵, 0행 인식하지 않음, Header 선언
# df=pd.read_csv('data/csv_s1.csv', skiprows=[0], header=None, names=["Month",2018,2019,2020])
# print(df)

# 행 스킵, 0행 인식하지 않음, Header 선언,  인덱스 컬럼 지정
# df=pd.read_csv('data/csv_s1.csv', skiprows=[0], header=None, names=["Month",2018,2019,2020], index_col=[0])
# print(df)
'''
#실습정리(가공)
df=pd.read_csv('data/csv_s1.csv', skiprows=[0], header=None, names=["Month",2018,2019,2020])
#print(df)
print('----------------------------------------------------')
print(df.index)
print('----------------------------------------------------')
print(df.rename(index=lambda x:x+1))
print('----------------------------------------------------')
print(df.rename(index=lambda x:x+1).index)
print('----------------------------------------------------')
print(df.index.values)
print('----------------------------------------------------')
print(df.index.values.tolist())
'''
df2 = pd.read_csv('data/csv_s2.csv', sep=';', skiprows=[0], \
                  header=None, names=["First name", 'Test1', 'Test2', 'Test3', 'Final', 'Grade'])
# print(df2)

# 합계
df2['Sum'] = df2[['Test1', 'Test2', 'Test3', 'Final']].sum(axis=1)  # axis=1:행단위
print(df2)

# 평균
df2['Age'] = df2[['Test1', 'Test2', 'Test3', 'Final']].mean(axis=1)
print(df2)
