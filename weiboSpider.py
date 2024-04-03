import requests

weibo_url = 'https://weibo.com/ajax/side/hotSearch'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}
response = requests.get(weibo_url,headers=headers)
print(response.status_code)
print(response.text)