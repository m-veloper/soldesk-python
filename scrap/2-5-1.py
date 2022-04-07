from urllib.parse import urljoin

baseUrl="http://test.com/html/a.html"

print(urljoin(baseUrl, "b.html"))
print( urljoin(baseUrl, "sub/c.html") )
print( urljoin(baseUrl, "../index.html") )
print( urljoin(baseUrl, "../img/hoge.png") )
print( urljoin(baseUrl, "../css/hoge.css") )

'''
#결과
http://test.com/html/b.html
http://test.com/html/sub/c.html
http://test.com/index.html
http://test.com/img/hoge.png
http://test.com/css/hoge.css
'''
