# 爬虫项目2(自动获取)
from urllib import request
import chardet

if __name__ == "__main__":
    response = request.urlopen("http://qiaoliqiang.cn/")
    html = response.read()
    charset = chardet.detect(html)#返回的是一个字典
    print(charset)#{'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
    html = html.decode(charset["encoding"])
    print(html)



