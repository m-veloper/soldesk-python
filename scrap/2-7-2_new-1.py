from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url = "http://finance.naver.com/sise/"
# utf-8 : 한글 깨짐, unicode_escape : 한글 깨짐
res = req.urlopen(url).read().decode('cp949')
# 중간 출력
# print(res)

soup = BeautifulSoup(res, "html.parser")

top10 = soup.select("#popularItemList > li > a")

# 파싱 확인
# print(top10)
print('네이버 주식 인기검색 종목 10위')
for i, e in enumerate(top10, 1):
    print('순위 : {}, 이름 : {}'.format(i, e.string))
