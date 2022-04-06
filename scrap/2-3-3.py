import sys
import io
import urllib.request
from urllib.parse import urlparse

# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
# sys.stderr = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

API = "http://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

values = {
    'ctxCd': '1012'
}
params = urllib.parse.urlencode(values)
# 요청
url = API + "?" + params
# 읽기
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)
