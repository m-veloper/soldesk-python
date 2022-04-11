# 2021-04-30 최종 수정
# 기본 daum 주식 사이트 : Ajax방식의 변경으로 인해 코드 수정
# pip3 install fake-useragent

from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import json
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# Fake Headers 정보
ua = UserAgent()

# 헤더정보
headers = {
    'User-Agent': ua.ie,
    'referer': 'http://finance.daum.net/'
}

# 주식 요청 url
url = "http://finance.daum.net/api/search/ranks?limit=10"
# print(req.get_full_url())
# print(req.get_method()) #Post or Get

# 요청
res = req.urlopen(req.Request(url, headers=headers)).read().decode('utf-8')
# ======================================================================
# 응답 확인
print('res : ', res)

rank_json = json.loads(res)['data']

# 중간 확인
print("중간 확인 : ", rank_json, '\n')
# ==============================================================================
for elm in rank_json:
    # print(type(elm))
    print('순위 : {}, 금액 : {}, 회사명 : {}' \
          .format(elm['rank'], elm['tradePrice'], elm['name']), )
