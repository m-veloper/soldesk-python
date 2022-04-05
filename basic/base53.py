def func1():
    a = 10
    print("func1()에서 a의 값 %d" % a)
    print("======================")


def func2():
    print("func2()에서 a의 값 %d" % a)


# 전역 변수
a = 20

# 메인
func1()
func2()
