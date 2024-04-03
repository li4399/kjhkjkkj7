import time

import requests
from jsonpath import jsonpath

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
}

listPage_URL = 'https://careers.tencent.com/tencentcareer/api/post/ByCategories?timestamp=1711024528051&language=zh-cn'
detail_URL = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1711024914523&countryId=&cityId=&bgIds=&productId=&categoryId={}001,{}002,{}003&parentCategoryId=&attrId=1&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
d2url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1711026560910&countryId=&cityId=&bgIds=&productId=&categoryId={}&parentCategoryId=&attrId=1&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'

def get_json(url):
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.json()
    raise Exception('接口请求异常')

def parse_listPage(listPage_jsonData):
    CategoryNames = jsonpath(listPage_jsonData,'$..CategoryName')
    CategoryIds = jsonpath(listPage_jsonData,'$..CategoryId')
    return CategoryNames,CategoryIds

def parse_detailPage(detailPage_Data,filename):
    pns = jsonpath(detailPage_Data,'$..RecruitPostName')
    wyns = jsonpath(detailPage_Data,'$..RequireWorkYearsName')
    f = open('tx/'+filename + '.txt', 'a')
    for pn, wyn in zip(pns,wyns):
        # print(pn,wyn)
        f.write(pn+'\t'+wyn+'\n')
    f.close()


if __name__ == '__main__':
    # 1、获取列表页数据并解析
    list_data = get_json(listPage_URL)
    # 解析列表页数据中的类别名、类ID
    CategoryNames, CategoryIds = parse_listPage(list_data)
    for name,pid in zip(CategoryNames, CategoryIds):
        print(f'当前正在抓取{name}岗位数据，PID：{pid}')
        for page_number in range(1, 4):     # 构造详情页的翻页参数
            print(f'当前正在抓取{name}岗位数据，第{page_number}页')
            # 请求具体类别的当前页的数据
            detail_data = get_json(detail_URL.format(pid,pid,pid,page_number))
            try:
                parse_detailPage(detail_data,name)
            except Exception:
                detail_data = get_json(d2url.format(pid,page_number))
                parse_detailPage(detail_data, name)
            # time.sleep(5)

