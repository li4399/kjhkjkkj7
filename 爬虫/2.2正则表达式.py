# 正则
# import re
# # a =re.search('\d+','wwccdww6666gv')
# # print(a)
#
# content = 'Hello word 2024'
# aaa = 'zhangsan 666'
# res = re.match('^\wello\s\w{4}.\d+$',content)
# res_1 = re.match('^\w{8}\s\d+$', aaa)
# res_2 = re.match('^H.*?2024$',content)
# print(res)
# print(res_1)
# print(res_2)

# import re
#
# html = '''<div id="songs-list">
#     <h2 class="title">经典老歌</h2>
#     <p class="introduction">
#         经典老歌列表
#     </p>
#     <ul id="list" class="list-group">
#         <li data-view="2">一路上有你</li>
#         <li data-view="7">
#             <a href="www.aaa.com/2.mp3" singer="任贤齐">沧海2声笑</a>
#         </li>
#         <li data-view="4" class="active">
#             <a href="/3.mp3" singer="齐秦">往事随风</a>
#         </li>
#         <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
#         <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
#         <li data-view="5">
#             <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
#         </li>
#     </ul>
# </div>'''
# # pe = '<a.*?>(.*?)</a>'
# pe = '<a.*?singer="(.*?)">'
# res = re.findall(pe,html,re.S)
# print(res)

import requests

url = "https://book.douban.com/latest?icn=index-latestbook-all"
qwe = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}
response = requests.get(url, headers=qwe)
# print(response.text)

import re

bsd = '<a.class="fleft".*?>(.*?)</a>'
book_name = re.findall(bsd,response.text)
print(book_name)

bsd = '<a.class="fleft".*?href="(.*?)">'
book_li = re.findall(bsd,response.text)
print(book_li)

bsd = '<p.class="subject-abstract.color-gray">(.*?)</p>'
book_xiangq = re.findall(bsd, response.text,re.S)
print(book_xiangq)