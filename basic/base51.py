import random


# 함수
def getNumber():
    return random.randrange(1, 46)


# 변수
lotto = []
num = 0

# 메인
print("** 로또 추첨을 시작합니다.**")

while True:
    num = getNumber()

    # 중복제거
    if lotto.count(num) == 0:
        lotto.append(num)

    if len(lotto) >= 6:
        break

print("추천된 로또 번호 ==> ", end="")
lotto.sort()
for i in range(0, 6):
    print("%d " % lotto[i], end= "")
