# pickle 모듈은 파이썬 객체를 파일로 저장하고 메모리로 읽어올 수 있도록 도와줌
# 객체를 저장한 상태에서 프로그램이 종료되면 객체 내용이 자동으로 소멸됨

import pickle

# f = open('setting.txt', 'wb')
# setting = [{'title': 'python program'}, {'author': 'sul'}]
# pickle.dump(setting, f)
# f.close()

# try
f = open('../setting.txt', 'wb')
try:
    setting = [{'title': 'python program'}, {'author': 'sul'}]
    pickle.dump(setting, f)
except Exception as e:
    print(e)
finally:
    f.close()
