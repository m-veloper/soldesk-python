from bs4 import BeautifulSoup
import requests
import sys
import io
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 요청
URL = 'https://www.wishket.com/accounts/login/'

with requests.Session() as s:
    s.get(URL)
    # Login 정보 Payload
    LOGIN_INFO = {
        'identification': 'smile516',
        'password': 'jinbin516@',
        'csrfmiddlewaretoken': s.cookies['csrftoken']
    }

    print('token', s.cookies['csrftoken'])
    print('headers', s.headers)  # 'User-Agent': 'python-requests/2.27.1' 확인됨
    # 요청
    response = s.post(URL, data=LOGIN_INFO)
    # 결과
    print('response', response.text)
