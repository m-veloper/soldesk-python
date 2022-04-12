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
    # Login 정보 Payload
    LOGIN_INFO = {
        'identification': 'smile516',
        'password': 'jinbin516@'
    }

    # 요청
    response = s.post(URL, data=LOGIN_INFO)
    # 결과
    print('response', response.text)
