# pip install requests
'''
TODO 爬虫初步体验
'''

import requests
# 1、发起请求
# 2、获取响应
url = "https://www.mi.com/shop"
response = requests.get(url)    # 发起请求
print(response.status_code)     # 获取状态码
print(response.text)            # 获取网页源码
