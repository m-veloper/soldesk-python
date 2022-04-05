import matplotlib.pyplot as plt

# 데이터의 정의
temperatures = [3.3, 34.5, 14.2, -10]
x = list(range(4))
x_labels = ['Spring', 'Summer', 'Fall', 'Winter']

# bar 차트
plt.title("Bar Chart")
plt.bar(x, temperatures)
plt.xticks(x, x_labels)  # x축 데이터 위치에 레이블 표시
plt.yticks(sorted(temperatures))
plt.xlabel("seasons")
plt.ylabel("temperatures")
plt.show()
