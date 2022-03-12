# coding:utf8
import requests

url = 'http://www.baidu.com'
res = requests.get(url)
res.encoding = 'utf-8'
print(res.text)
