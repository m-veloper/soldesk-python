import errno

from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

opener = req.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
req.install_opener(opener)

# Html 가져오기
base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("사자")
url = base + quote

res = req.urlopen(url)
savePath = "D:/python/img/"

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:  # 디렉토리가 있다면
    if e.errno != errno.EEXIST:  # 파일이 존재할 경우
        print("Failed to create directory!!")
        raise  # 컴파일 확인

soup = BeautifulSoup(res, "html.parser")
print(soup)

li_list = soup.select(
    "#main_pack > div > div.photo_group._listGrid > div.photo_tile._grid > div:nth-child(3) > div > div.thumb > a > img")
print(li_list)

for i, div in enumerate(li_list, 1):
    print(div)
    fullfilename = os.path.join(savePath, savePath + str(i) + '.jpg')
    print(fullfilename)
    req.urlretrieve(div['data-source'], fullfilename)
    print()

print('다운로드 완료')
