# 함수
def func1():
    result = 100
    return result


def func2():
    print("반환값이 없는 함수")


## --------------------------------
# 변수
sum = 0

# 메인
sum = func1()
print("func1() ==> %d" % sum)
func2()
