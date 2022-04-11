from bs4 import BeautifulSoup
import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

with requests.Session() as s:
    post_one=s.get('https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=201719&target=after')
    soup=BeautifulSoup(post_one.text, 'html.parser')
    #print(soup)

li=soup.select('td.title')
#print(li)


for i in li:
    print(i.select_one('em').string)
    print(i.find('br').next_sibling.string.strip())
    print("======================================================")
