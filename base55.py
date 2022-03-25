inFp, outFp = None, None
inStr, outStr = "", ""

inFp = open('c:/Windows/notepad.exe', 'rb')
outFp = open('c:/temp/notepad.exe', 'wb')

while True:
    inStr = inFp.read()
    if not inStr:
        break
    outFp.write(inStr)

inFp.close()
outFp.close()

print("바이너리 파일 복사 완료!")
