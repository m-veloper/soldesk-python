import requests
from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

with requests.Session() as s:
    #게시글 가져오기
    post_one=s.get('https://bbs.ruliweb.com/market/board/1020/read/37546')

    #예외발생
    post_one.raise_for_status
    #예외 발생시 출력
    #print(post_one.text)

    soup=BeautifulSoup(post_one.text, 'html.parser')
    #print(soup.prettify)

    #문서만 출력
    article=soup.select("#board_read > div > div.board_main > div.board_main_view > div.view_content > article > div > p")
    #print(article)

    #String 처리
    for i in article:
        if i.string is not None and i.img == None:
            print(i.string)  
