import sys
import io
import urllib.request
from urllib.parse import urlparse

# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
# sys.stderr = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

API = "https://api.ipify.org"

values = {
    'format': 'json'
}

print('before', values)

params = urllib.parse.urlencode(values)

print('after', params)

# 요청
url = API + "?" + params

print("요청 URL", url)

# 읽기
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)
