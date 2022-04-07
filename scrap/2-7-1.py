#2021-04-30 수정된 코드(Ajax)

from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import json
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#Fake Header정보
ua=UserAgent()

#헤더정보
headers={
    'User-Agent':ua.ie,
    'Referer': 'http://finance.daum.net/'
}

#주식 요청 (Top 10)
url="http://finance.daum.net/api/search/ranks?limit=10"
#print(request.get_full_url())
#print(request.get_method())

#요청
res=req.urlopen(req.Request(url, headers=headers)).read().decode('utf-8')

#응답
print('res',res)
# json 형태로 데이터 바꾸기
rank_json=json.loads(res)['data']

print("중간 확인 : ",rank_json, '\n')

for elm in rank_json :
    #print(type(elm))
    print('순위 : {},금액 : {}, 회사명 : {}'.format(elm['rank'],elm['tradePrice'],elm['name']))
