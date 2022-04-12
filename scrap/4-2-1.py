from bs4 import BeautifulSoup
import urllib.request as req
import os.path
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 데이터 수집 (https://www.weather.go.kr/w/pop/rss-guide.do)
url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4128551000"
savename = "data/forecast1.xml"

if not os.path.exists(savename):
    req.urlretrieve(url, savename)

xml = open(savename, "r", encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')
# 분석
for location in soup.find_all("data"):
    loc = location.find("hour").string
    print(loc)
    weather = location.select_one("wfKor").string
    print(weather)

# with문으로 저장
with open("data/cast1.txt", "wt", encoding="utf-8") as f:
    title = soup.find("category").string
    f.write('지역 => {} \n\n'.format(title))
    for location in soup.find_all("data"):
        loc = location.find("hour").string
        weather = location.select_one("wfKor").string
        f.write('시간 : {}, 날씨 : {} \n'.format(loc, weather))
