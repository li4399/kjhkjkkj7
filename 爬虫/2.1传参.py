import requests
# import json
# url = "http://httpbin.org/get"
# data = {
#     'name':'list',
#     'age':22,
#     'sex':'man'
# }
# response = requests.get(url, params =data)
# print(response.text)
#
# print(response.json())

url = "https://www.jianshu.com/"
# 请求头
qwe = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}
response = requests.get(url, headers=qwe)
print(response.status_code)
print(response.text)

