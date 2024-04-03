import requests
from bs4 import BeautifulSoup

url = 'https://www.maoyan.com/board/4?timeStamp=1710558911288&channelId=40011&index=10&signKey=22072276911f3bab3efa966be66502a5&sVersion=1&webdriver=false'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}
res = requests.get(url, headers=headers)
html = res.text

doc = BeautifulSoup(html, 'lxml')
srts = doc.find_all('dd')
names = doc.find_all('p',{'class': 'name'})
stars = doc.find_all('p', {'class': 'star'})
up_time = doc.find_all('p', {'class': 'releasetime'})

for n,s,t, srt in zip(names,stars,up_time,srts):
    print(srt.i.string)
    print(n.a.string.strip())
    print(n.a['href'])
    print(s.string.strip())
    print(t.string.strip())
    print('---'*20)

