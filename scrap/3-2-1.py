import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
'''
s=requests.Session()
r=s.get('https://www.naver.com') #Get,put,Delete, Post
print('1', r.text)
s.close()
'''
#with
with requests.Session() as s:
    r=s.get('https://www.naver.com')
    #print('1', r.text)

#test보내고 응답을 받음
'''
r=s.get('http://httpbin.org/cookies',cookies={'from':'myName'})
print(r.text)
s.close()
'''
#with 문 변경
with requests.Session() as s:
    r = s.get('http://httpbin.org/cookies',cookies={'from':'myName'})
    print(r.text)
print("================================")
url = 'http://httpbin.org/get'
headers = {'user-agent':'myPythonApp_1.0.0'}

'''
r = s.get(url,headers=headers)
print(r.text)
s.close()
'''
# with문 변경
with requests.Session() as s:
    r = s.get(url,headers=headers)
    print(r.text)
