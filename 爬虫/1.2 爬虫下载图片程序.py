'''

抓图片，保存到本地
'''

import requests

# img_url = 'https://www.baidu.com/img/PCfb_5bf082d29588c07f842ccde3f97243ea.png'
#
# response = requests.get(img_url)
# print(response.status_code)
# print(response.content)
#
# f = open('1.png', 'wb')
# f.write(response.content)
# f.close()


img_list = [
    "https://www.baidu.com/img/PCfb_5bf082d29588c07f842ccde3f97243ea.png",
    "https://c-ssl.dtstatic.com/uploads/blog/202205/07/20220507115721_79dc7.thumb.1000_0.jpg"
]

number = 1  # 自增变量 用于图片命名
for url in img_list:    # 循环 遍历图片列表 拿到每一个url给requests请求
    print(url)  # 获取到的每一个url链接
    res = requests.get(url) # 请求并获取数据
    file_name = ''+str(number)+'.png'   # 构建文件名
    f = open(file_name, 'wb')   # 写入 保存到文件
    f.write(res.content)
    f.close()
    number += 1 # 自增 +1