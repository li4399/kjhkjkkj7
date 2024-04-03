import time

from selenium import webdriver
from selenium.webdriver.common.by import By  # 封装了一些查找器
from selenium.webdriver.common.keys import Keys  # 封装了一些功能按钮
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
'''
1、打开百度
2、在搜索框输入Python
3、点击搜索按钮
'''
browser = webdriver.Chrome()  # browser 驱动对象
# try:
# 1 打开百度
browser.get('https://www.maoyan.com/board/4')  # 调用浏览器驱动对象访问站点
ele_list = browser.find_elements(By.CLASS_NAME,'name') # []
# print(ele_list)
# time.sleep(3)
href_list = []
for ele_title in ele_list:
    href = ele_title.find_element(By.TAG_NAME,'a').get_attribute('href')
    href_list.append(href)

for href in href_list:
    browser.get(href)
    time.sleep(1.2)

# print(browser.page_source)
time.sleep(1000)


