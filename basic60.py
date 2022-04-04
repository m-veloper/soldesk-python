# 클래스 정의 부분
class Car:
    color = ""
    speed = 0
    count = 0

    def printMessage(self):
        print("테스트 출력")

    # 생성자
    def __init__(self):
        self.speed = 0
        Car.count += 1


# 변수 선어ㅗㄴ
myCar1, myCar2 = None, None

# 메인

myCar1 = Car()
myCar1.speed = 30

print("자동차1의 속도는 %d km고, 생상된 자동차의 수는 %d대 입니다." % (myCar1.speed, Car.count))
