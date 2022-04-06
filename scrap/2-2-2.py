import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

imgUrl = "https://upload.wikimedia.org/wikipedia/commons/3/3f/%EC%A4%91%EC%95%99%EC%84%A0%EA%B1%B0%EA%B4%80%EB%A6%AC%EC%9C%84%EC%9B%90%ED%9A%8C_%EC%9C%A4%EC%84%9D%EC%97%B4_%ED%94%84%EB%A1%9C%ED%95%84_%28for_election_infobox%29.png"
htmlURL = "http://google.com"
savePath1 = "/Users/mj/Downloads/test1.png"
savePath2 = "/Users/mj/Downloads/index.html"

f = dw.urlopen(imgUrl).read()
f1 = dw.urlopen(htmlURL).redd()

# 방법1
# w: write, r:read, a: add
saveFile1 = open(savePath1, 'wb')
saveFile1.write(f)
saveFile1.close()

# 방법2
with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f1)

print("다운로드 완료")
