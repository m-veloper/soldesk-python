import sys
import io
from bs4 import BeautifulSoup
import urllib.request as req
import os.path

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 요청
url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4711369000'

savename = 'data/forecast2.xml'

if not os.path.exists(savename):  # 없으면 만들어라
    req.urlretrieve(url, savename)

# 숲처리
xml = open(savename, 'r', encoding='utf-8').read()
soup = BeautifulSoup(xml, 'html.parser')
# print(soup)
info = []
b = []
'''
#분석 확인
for first_item in soup.find_all("data"):
    #print(first_item)
    day_item=first_item.find("day").string
    time_item=first_item.find("hour").string
    temp_item=first_item.find("temp").string

    a='포항시 북구 두호동의 4월 {}일 {}시 기온은 {}도 입니다'.format(str(int(day_item)+1),time_item,temp_item)
    #print(a)
'''
# with문으로 저장
with open("data/cast2.txt", "wt", encoding="utf-8") as f:
    title = soup.find("category").string
    f.write('지역 => {} \n\n'.format(title))
    for first_item in soup.find_all("data"):
        day_item = first_item.find("day").string
        time_item = first_item.find("hour").string
        temp_item = first_item.find("temp").string
        f.write('포항시 북구 두호동의 4월 {}일 {}시 기온은 {}도 입니다'.format(str(int(day_item) + 1), time_item, temp_item) + '\n')

print('저장완료')
