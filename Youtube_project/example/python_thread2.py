import threading

#쓰레드 상속 실행 - 클래스

class Thread_Run(threading.Thread):
    def run(self): #상속받은 메소드
        print('Thread running - C')


for i in range(1000):
    t=Thread_Run()
    t.start()
