url_a = 'https://www.y2mate.com/mates/analyzeV2/ajax'
vid = input("请输入要下载的视频VID:")
a_data = {
    "k_query": f"https://www.youtube.com/watch?v={vid}",
    "k_page": "home",
    "hl": "en",
    "q_auto": "1",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

import requests, json
from jsonpath import jsonpath

res = requests.post(url_a, data=a_data, headers=headers)
print(res.status_code)
data_dt = res.json()
kss = data_dt['links']['mp4']
print(kss.keys)
k = data_dt['links']['mp4']['160']['k']
print(k)

url_b = 'https://www.y2mate.com/mates/convertV2/index'
data_b = {
    "vid": vid,
    'k': k
}

res_b = requests.post(url_b, data=data_b,headers=headers)
print(res_b.status_code)
dlink = res_b.json()['dlink']

video_data = requests.get(dlink,headers=headers).content
f = open(vid+'.mp4','wb')
f.write(video_data)
f.close()
