from bs4 import BeautifulSoup
import re #정규식
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
  <ul>
    <li id="naver"><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="http://www.daum.com">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""

soup = BeautifulSoup(html, "html.parser")
naver=soup.find(id="naver")
print("id:naver >> " ,naver.string)
#정규식코드 이용하는 분석
li1=soup.find_all(href=re.compile(r"da"))
print("li1 => ", li1)
li2=soup.find_all(href=re.compile(r"^https://"))
print("li2 => ", li2)
#속성으로 분석
for e in li2:
    print(e.attrs['href'])
