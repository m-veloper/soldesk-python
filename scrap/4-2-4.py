import sys
import io
from bs4 import BeautifulSoup
import urllib.request as req
import os.path

# 한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 요청
url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'

savename = 'data/forecast5.xml'
if not os.path.exists(savename):  # 없으면 만들어라
    req.urlretrieve(url, savename)

# 숲처리
xml = open(savename, 'r', encoding='utf-8').read()
soup = BeautifulSoup(xml, 'html.parser')
# print(soup)

# 지역확이
info = {}  # info = {"서울": [11,17,8,1.-1]}
for location in soup.find_all("location"):
    loc = location.find("city").string
    # print(loc)
    weather = location.find_all("tmn")
    # print(weather)
    if not (loc in info):  # 중복확인
        info[loc] = []
    for tmn in weather:
        info[loc].append(tmn.string)  # 값 11,17,10,-1 ..
'''
print(info)
print(info.keys())
print(list(info.keys()))
print(info.values())
'''

with open("data/forecast6.txt", "wt", encoding="utf-8") as f:
    for loc in sorted(info.keys()):
        # print("지 역 : ",loc)
        f.write('\n' + str(loc) + '\n')
        for name in info[loc]:
            # print("기 온 : ",name)
            f.write('\t' + str(name) + '\n')

print('분석 저장 완료')
