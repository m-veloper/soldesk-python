import urllib.request as req
import os.path, random
import simplejson as json

# URL 요청
url = "https://api.github.com/repositories"

# 경로와 파일명 (repo.json)
savename = "D:/BIG_DATA/section4/repo.json"

# 예외처리 (파일존재 확인)
if not os.path.exists(url):
    req.urlretrieve(url, savename)

# 객체로 역직렬화(load)
# items=json.load(open(savename, 'r', encoding="utf-8"))
# 문자로 역직렬화(loads)
items = json.loads(open(savename, 'r', encoding='utf-8').read())

# 출력 (console 출력)
print(type(items))

for item in items:
    # print(item)
    print(item["full_name"] + " - " + item["owner"]["url"])
