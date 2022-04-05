# 읽기 : read = open("in.txt", "r")
# 쓰기 : write = open("in.txt", "w")
# 읽기 : r
# 쓰기 : w
# 읽기/쓰기 : r+
# 이어 쓰기 : a
# 텍스트 : t
# 바이 너리 : b

import os

path = "c:/temp/"
dirContents = os.listdir(path)


def save_file():
    for i in dirContents:
        if os.path.isfile(path + i):
            print("파일을 찾았습니다.")
            tmp = input("복사를 하시겠습니까(y/n)?")

            if tmp == "y":
                input_file = open(path + i + "", encoding="utf-8")
                buffer = input_file.read()

                output_file = open(path + input("저장할 파일 이름을 입력하세요 : ") + ".txt", "w", encoding="utf-8")
                enc = input("암호화 하시겠습니까(y/n)?")

                if enc == "y":
                    output_file.write(encrypt(buffer))
                else:
                    output_file.write((buffer))

                output_file.close()
                input_file.close()

            else:
                print("종료합니다.")


# 암호화
def encrypt(string):
    # 암호 문서 판독
    crypt = chr(0x110000 - 1)

    for i in string:
        crypt += chr(ord(i) * 17)

        return crypt


# 검증
def isEncrypt(string):
    result = False
    if ord(string[0]) == 0x110000 - 1:
        result = True

    return result


# 복호화
def decrypt(string):
    decrypt = ""

    for i in string:
        decrypt += chr(int(ord(i) / 17))

    return decrypt


# 파일 불러오기
def decrypt_file():
    for i in dirContents:
        if os.path.isfile(path + i):
            file = open(path + i, "r", encoding="utf-8")
            buffer = file.read()

        # 암호화된 파일인가?
        if isEncrypt(buffer):
            Output = open(path + i + "_decrypt", + ".txt", "w", encoding="utf-8")

            # 복호화
            Output.write(decrypt(buffer))
            Output.close()

        else:
            print("암호화 되어있지 않습니다.")
            file.close()

    # 메인
    save_file()
    decrypt_file()
