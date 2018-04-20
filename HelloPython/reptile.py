# 爬虫项目
from urllib import request

if __name__ == "__main__":
    response = request.urlopen("http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%CC%AB%D4%AD%BF%C6%BC%BC%B4%F3%D1%A7%CD%BC%C6%AC&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=000000")
    html = response.read()
    html = html.decode("utf-8")
    print(html)




