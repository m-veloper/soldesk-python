# 함수
def para2_func(v1, v2):
    result = 0
    result = v1 + v2
    return result


def para3_func(v1, v2, v3):
    result = 0
    result = v1 + v2 + v3
    return result


# ===================
hap = 0

# 메인
hap = para2_func(10, 20)
print("매개변수 2개  ==> %d" % hap)
hap = para3_func(10, 20, 30)
print("매개변수 3개  ==> %d" % hap)
