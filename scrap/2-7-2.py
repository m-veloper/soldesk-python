
from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://finance.naver.com/sise/"
res = req.urlopen(url).read().decode('euc-kr')
soup = BeautifulSoup(res, "html.parser")

top = soup.select("#siselist_tab_0 > tr")

#방법1
i=1
for e in (top):
    #print(e)
    if e.find("a") is not None :
        print(i,e.select_one(".tltle").string)
        i+=1

#방법2
print('Top 10 종목명 출력 ')
for i, e in enumerate(top):
    if e.find("a") is not None :
        i-=1
        if i>=9:
            i=i+3
        print(i,e.select_one(".tltle").string)

print('Top 10 현재가 출력')
i = 1
for e in top:
    if e.find("a") is not None:
        print(i,e.select_one(".tltle").string,"=", \
        e.select_one("td:nth-of-type(5)").string)
        i += 1
