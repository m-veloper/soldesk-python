import time

print(time.time())
print(time.localtime(time.time()))

t = time.localtime(time.time())
print(time.strftime('%y/%m/%d - %H:%M:%S', t))
