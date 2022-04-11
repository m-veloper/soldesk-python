import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

'''
r = requests.get('https://api.github.com/events')
r.raise_for_status()
print(r.text)

jar = requests.cookies.RequestsCookieJar()
jar.set('name','kim',domain='httpbin.org',path='/cookies')

r = requests.get('http://httpbin.org/cookies',cookies=jar)
r.raise_for_status()
print(r.text)
'''
payload1 = {'key1': 'value1', 'key2': 'value2'} #dict
payload2 = (('key1','value1'),('key2','value2')) #tuple
payload3 = {'some':'nice'}

r = requests.put('http://httpbin.org/put', data=payload1)
print(r.text)

r = requests.put('https://jsonplaceholder.typicode.com/posts/1',data=payload1)
print(r.text)

r = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print(r.text)

# RestFul : get : (가져오기)  / post(fetch) :등록하기 / put : 수정 / delete : 삭제
