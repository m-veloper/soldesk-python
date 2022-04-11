import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#Response 상태 코드
s = requests.Session()
r = s.get('http://httpbin.org/get')
print(r.status_code)
print(r.ok)

r = s.get('https://jsonplaceholder.typicode.com/posts/1')
print('1 : ',r.text)
print('2 : ',r.json())
print('3 : ',r.json().keys())
print('4 : ',r.json().values())
print('5 : ',r.encoding)
print('6 : ',r.content)
print('7 : ',r.raw)
