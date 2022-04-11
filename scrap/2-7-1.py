#2021-04-30 수정된 코드(Ajax)

from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url="http://finance.daum.net/"

res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")

top = soup.select("ul#boxTopSearchs > li")

for i,e in enumerate(top,1):
    print(i,e.find("a").string, "=", e.find("span").string)
