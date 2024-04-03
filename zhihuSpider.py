import requests
from lxml import etree
from jsonpath import jsonpath

zhihu_url = "https://www.zhihu.com/hot"
weibo_url = 'https://weibo.com/ajax/side/hotSearch'
bb_url = "https://api.bilibili.com/x/web-interface/popular?ps=20&pn={}&web_location=333.934&w_rid=5461c04fb0130219654f2208592ae04b&wts=1711020999"

headers = {
    'Cookie':'_zap=e977cafa-9640-41e5-b1d4-1abc39e646ca; d_c0=AODSzkE5RxePTh5JyxQURh6r9wJLpeTsKVo=|1692696730; _xsrf=92EcwLgUeYv3leJ1X4d4dZzyB2gjIsFT; YD00517437729195%3AWM_NI=qEs4cIvF2Wx1tLsLsGIEeWVN6U2QS5gSUOTKjjdyCi0tR0BPXZUCUb50Mw66HleWhtRlk9fQNuqs8RS9wpvFZTFkqJ1tSAuHLmkYxmuBklzt%2FXafmVJo9mDKX5zh959JcGo%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eea2d140fcbfa48ad545b4eb8fb6d54e978f8fb1c872aef1c083c64288888db6ea2af0fea7c3b92ab39bbdd5e243b69afeb8fb3bb894bdadf24d8b9babb8d546f68bfeb2d23fa58d9bb0d741aab6ac9ac263f4ac9ed1c15c9c869ba4d86af7f08398b53e8cb4abb8eb8092b4a5dae55b8eabbf94bb5a91e7b991f54e9a8c8a8cf442f3ac9da2f84490b3a5bafb67b79ea58df980ed88af87f05e8ab1f78ec7419cebb689bc3ffb96ada8ee37e2a3; YD00517437729195%3AWM_TID=Z3Ml3GZvQZFAAFAQQQeB2jupaTMDTDAl; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1698632621,1698840529,1698841035,1699577596; captcha_session_v2=2|1:0|10:1712058146|18:captcha_session_v2|88:bnUvZjVaTTdYTDRvUW1LYU8zQmhuK3NUOWVMOWZSck5hS1IzZWhQbjQ5OFZMczErQ0ZUTzhITkwvbW9hZHJ2Tg==|54a707c982e1bb63dae4315f3f7e368a3f6774e8f029583bfdf7ee10583846a8; __snaker__id=mrG4x1SOzHap1D1C; gdxidpyhxdE=GI3O2U3rTMk6fNOYua20r%5Ci%2FPe3aVyXOcyb1eGA81NRMeYrmPwM9PH0aE1JNXSBSIByPzBjrId5s%2FAzLUl8P2%2B4Cu1V%5C%2BgpqI%2BjLyAqiCBRcpj2uLrq9sl9NGSXyvMrS%5CW0M%2B081XD1A5CsL17aY%5C1XmgplgahUv7N%5ChTCZSAAsi%2B7oH%3A1712059053547; captcha_ticket_v2=2|1:0|10:1712058164|17:captcha_ticket_v2|728:eyJ2YWxpZGF0ZSI6Ik5BTlBfYkdzZGZmUEVrVmtXYVpBdWpoMlhha0NzWWJ6OWxMZkhjcS5nZVZPcFVwbzVMY2hOcGxTcVpMNW5TTTl6Q2ZMemxCSlhhUnY4Nk8zS2Zkc1pyYkp5NHo2UWpxb01oUDJhNmJ5XzJYQVQxUFYwZmxMc0FyMnc5S1M2TEVTYm5mbU1xanN4cG9WVnRuamp6S0JncWVwSFkyVTVqenkzdlA4QVYxaGM1ZG56aTlOZ0tWYUxISkFCRXlxRjhwXzk0dWtuT2VPUDNJMHBkU2dZcWxpTGZzTmtPci5kMFFFM0ZxUVVYcEExRndybndYSlRHVEhjanRRTDB5QypMYWR2QnE1R1FxKkQ2dENLQ2dhc0pwMi5zbGJCUEEqXzVMOEsyY1Z1dlhRd0FCRkUzMUw2clZqa3pWV3JibnJwV2RKeG1LTEVWTHhuUDBNbzgydWNlSXljNmJhZWplZjNRbzRjMHdSVW1DRy5mRVF1aFlyZHRicmdaWVg2d3BvdmprSDhfWkVIQW9MRlU5UzNEb0tteExpaVd1ODJRbEhEZ084KmRQRDlROUR1Y20qNjhxUkNxcWdNZG0wcTBReDNralphdTJmVmlzNU1sWUFfYU5hZjN5b0xhYU5IalYxbVd2SnpzTURHaEM2eXEqTUpPb3IuSklZbnpXNW5lYkZYM2hVb1dwVEQ2UGdVU1g3N192X2lfMSJ9|62373b6b470504673a46e4da8620224e27715f11df570c2877592a7e4588d709; z_c0=2|1:0|10:1712058181|4:z_c0|92:Mi4xVjhFSE5BQUFBQUFBNE5MT1FUbEhGeVlBQUFCZ0FsVk5SVDM1WmdEUUp0NVNIUWluREQzeDlUenFMZFJpRzNwYkx3|a6197f3dca162a4fc1a98175a1f50dd5c04f9cb8d6345202e57c2909055b3511; q_c1=dcc2b23016ad406592e15f47a56f3fce|1712058182000|1712058182000; tst=h; SESSIONID=IVolAPxdJRT6IfCUwnLwQQlG9Fdgl8vVwKiDNdGlktT; KLBRSID=c450def82e5863a200934bb67541d696|1712058192|1712058026',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

url_list = [zhihu_url, weibo_url, bb_url]

def get_data(url, headers):
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response
    raise Exception(f'error status_code: {response.status_code}')

def parse_zhihu(zhihu_data):
    doc = etree.HTML(zhihu_data)


def parse_weibo(zhihu_data):
    pass

def parse_bb(zhihu_data):
    pass

if __name__ == '__main__':
    for i in range(1,11):
        print(f'正在抓取第{i}页')
        data = get_data(zhihu_url)
        parse_data(data)