import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


brower = webdriver.Chrome()

brower.get('https://www.baidu.com')
text_input = brower.find_element(By.ID,'kw')
text_input.send_keys('python')
# text_input.send_keys(Keys.ENTER)
brower.find_element(By.ID,'su').click()
time.sleep(10)


import pymysql
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123456',
    'port':3306,
    'database':'book'
}
conn = pymysql.Connect(**config)
cur = conn.cursor()
sql = 'select * from book'
cur.execute(sql)
print(cur.fetchall())