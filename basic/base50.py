# 함수
def para_func(v1, v2, v3=0):
    result = 0
    result = v1 + v2 + v3
    return result


# ===================
sum = 0

# 메인
hap = para_func(10, 20)
print("매개변수 2개  ==> %d" % hap)
hap = para_func(10, 20, 30)
print("매개변수 3개  ==> %d" % hap)

print("==================================")


def para1_func(*para):
    result = 0
    for num in para:
        result = result + num
    return result


# ===================
sum = 0

# 메인
hap = para1_func(10, 20)
print("매개변수 2개  ==> %d" % hap)
hap = para1_func(10, 20, 30)
print("매개변수 3개  ==> %d" % hap)
