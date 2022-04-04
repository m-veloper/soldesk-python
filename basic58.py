# 클래스
class Car:
    color = ""
    speed = 0

    def upSpeed(self, value):
        self.speed += value

    def upSpeed(self, value):
        self.speed -= value


# 메인
# 자바 -> Car mycar1 = new Car()
# 객체 생성
myCar1 = Car()
myCar1.color = "빨간색"
myCar1.speed = 0

myCar2 = Car()
myCar2.color = "파란색"
myCar2.speed = 0

myCar3 = Car()
myCar3.color = "노란색"
myCar3.speed = 0

myCar1.upSpeed(30)
print("자동차1의 색상은 %s이며, 현재 속도는 %d km입니다." % (myCar1.color, myCar1.speed))

myCar1.upSpeed(60)
print("자동차1의 색상은 %s이며, 현재 속도는 %d km입니다." % (myCar1.color, myCar1.speed))

myCar1.upSpeed(10)
print("자동차1의 색상은 %s이며, 현재 속도는 %d km입니다." % (myCar1.color, myCar1.speed))
