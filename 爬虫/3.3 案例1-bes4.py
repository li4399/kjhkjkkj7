import requests
from bs4 import BeautifulSoup

url = "https://movie.douban.com/top250?start="

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}

res = requests.get(url, headers=headers)
html_data = res.text

doc = BeautifulSoup(html_data, 'lxml')
titles = doc.find_all('span', {'class': 'title'})
for tit in titles:
    print(tit.string.split('/')[0])

pes = doc.find_all('div', {'class':'bd'})
for pe in pes:
    print(pe.p.string)




