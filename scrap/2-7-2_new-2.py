from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url = "https://issuenow.musttry.co.kr/"
# utf-8 : 한글 깨짐, unicode_escape : 한글 깨짐
res = req.urlopen(url).read()
# 중간 출력
# print(res)

soup = BeautifulSoup(res, "html.parser")

top10 = soup.select("#__next > div > div > main > div > div:nth-child(2) a")

# 파싱 확인
# print(top10)
print('실시간 인기검색 종목 20위')
for i, e in enumerate(top10, 1):
    print('순위 : {}, 제목 : {}'.format(i, e.string))
