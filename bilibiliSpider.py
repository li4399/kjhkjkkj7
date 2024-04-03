import requests
bb_url = 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all&web_location=333.934&w_rid=d9dd79815e19908e5eeaba28dd58623d&wts=1712057009'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

response = requests.get(bb_url, headers=headers)
print(response.status_code)
print(response.text)