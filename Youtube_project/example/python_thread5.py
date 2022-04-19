import threading
import time



def thread_run():
    print('====',time.ctime(), '=====')
    for i in range(1, 50001):
        print('Thread running - ', i)

#메인
threading.Timer(7, thread_run).start()
