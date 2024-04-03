import requests
import re

url = "https://movie.douban.com/top250?start="

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}

def getHtml(url,page_number):
    print("正在获取第"+str((page_number+25)//25)+"页")
    res = requests.get(url, headers=headers)
    print(res.status_code)
    html_data = res.text
    # bsd = '<div.class="hd".*?<a.*?<span.*?>(.*?)</span>.*?<span.*?>(.*?)</span>.*?<span.*?>(.*?)</span>.*?</a>'
    bsd = '<div.class="hd".*?<a.*?<span.*?>(.*?)</span>.*?</a>'
    film_name = re.findall(bsd,html_data,re.S)
    print(film_name)

url2 = "https://movie.douban.com/top250?start={}&filter="
# 手动构造页码 抓取所有数据
for page_number in range(0,250,25):
    new_url = url2.format(page_number)
    # f"https://movie.douban.com/top250?start={page_number}&filter="
    getHtml(new_url,page_number)

