import sys
import io
from bs4 import BeautifulSoup
import urllib.request as req
import os.path

# 한글 깨짐방지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 요청
url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1111061500'

savename = 'data/forecast3.xml'

if not os.path.exists(savename):  # 없으면 만들어라
    req.urlretrieve(url, savename)

# 숲처리
xml = open(savename, 'r', encoding='utf-8').read()
soup = BeautifulSoup(xml, 'html.parser')
# print(soup)

# 방법 1
# 확인
for data in soup.find_all("data"):
    hour = data.find("hour").string
    temp = data.find("temp").string
    # print(hour, ' ',temp)

with open("data/cast3.txt", "wt", encoding="utf-8") as f:
    for data in soup.find_all("data"):
        day = data.find("day").string
        f.write(str(int(day) + 1) + " 일차"'\n')
        hour = data.find("hour").string
        f.write("시간 : " + str(hour) + " 시"'\n')
        temp = data.find("temp").string
        f.write("온도 : " + str(temp) + "  도"'\n')
        wfKor = data.select_one("wfKor").string
        f.write("날씨 : " + str(wfKor) + '\n')
        pop = data.find("pop").string
        f.write("강수확율 : " + str(pop) + " %" + '\n')
        reh = data.find("reh").string
        f.write("습도 : " + str(reh) + " %" + '\n')
        f.write('\n')

# 방법 2
area = soup.find('category').string
d = soup.select_one('pubDate').string
tm = soup.select_one('tm').string
print(area)
print(d)
print(tm)
month_ = tm[4:6]
day_ = int(tm[6:8])
print(month_)
print(day_)

with open("data/forecast4.txt", "wt", encoding="utf-8") as f:
    f.write("지  역 : " + area + '\n')
    f.write("작성일자 : " + d + "\n\n")
    for data in soup.find_all("data"):
        dayplus = data.find("day").string
        hour = data.find("hour").string
        temp = data.find("temp").string
        wfKor = data.select_one("wfKor").string
        print("{}의 {}월 {}일 {}시 기온은 {}도 입니다.".format(area, month_, (day_ + int(dayplus)), hour, temp))
        f.write("{}의 {}월 {}일 {}시 기온은 {}도 입니다.\n".format(area, month_, (day_ + int(dayplus)), hour, temp))
