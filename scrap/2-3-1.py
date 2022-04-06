import sys
import io
import urllib.request
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

url = "http://www.encar.com/"
mem = urllib.request.urlopen(url)

print(type(mem))
print("getUrl : ", mem.geturl())
print("status : ", mem.status)
print("header : ", mem.getheaders())
print("info : ", mem.info())
print("code : ", mem.getcode(), "\n")
print("getCode : ", mem.getcode())
print("read : ", mem.read(10).decode('utf-8'))
print("parse : ", urlparse("http://www.encar.co.kr?test=test").query)
