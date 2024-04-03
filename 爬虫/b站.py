import requests
from jsonpath import jsonpath

url = "https://api.bilibili.com/x/web-interface/popular?ps=20&pn={}&web_location=333.934&w_rid=5461c04fb0130219654f2208592ae04b&wts=1711020999"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Cookie": "buvid3=F8D9075D-495B-AB9C-2F45-17283698F3D095169infoc; b_nut=1692013095; i-wanna-go-back=-1; b_ut=7; _uuid=E8A944ED-576D-229F-DDCF-F710D2B787D5E94551infoc; home_feed_column=4; buvid4=EC80035C-E1D5-8C05-8C25-DE1E6D34CBEC96090-023081419-%2BhGGnoawvNj5SvDjvc6zzbzNa7Gp4ky4gat4oqOobIORfndCeW1FsA%3D%3D; header_theme_version=CLOSE; buvid_fp_plain=undefined; LIVE_BUVID=AUTO8716920143575271; hit-new-style-dyn=1; hit-dyn-v2=1; rpdid=0zbfVGhj9Q|DuJJisVx|4EW|3w1QvXQl; is-2022-channel=1; iflogin_when_web_push=0; PVID=1; browser_resolution=1232-598; CURRENT_QUALITY=80; blackside_state=0; CURRENT_BLACKGAP=0; DedeUserID=261766594; DedeUserID__ckMd5=6bba22c4a94b99fb; enable_web_push=DISABLE; fingerprint=ecb956c9eed5fc6445eec9ef199effbb; buvid_fp=ecb956c9eed5fc6445eec9ef199effbb; FEED_LIVE_VERSION=V_WATCHLATER_PIP_WINDOW2; CURRENT_FNVAL=4048; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTEyMDk0MDgsImlhdCI6MTcxMDk1MDE0OCwicGx0IjotMX0.gkcb8jj8WA-g1Mivcq_65KDJ8loypEXPuo90ZZHzefY; bili_ticket_expires=1711209348; SESSDATA=fcce667a%2C1726502209%2Cdbcb6%2A32CjCjNEmR4AfGY9BGknp464C9AnDG4_wjs6fXAlzhT-xJ9xN2AK3KiP4aD4aCHHjCKUkSVmdmaXE3SUpWMDloazYyMy1YQ1RKcTRPMGtMVjFfX3VWMVAzZ2lEXy0yZ1pSRVVwaTM0c0dTZFJydVBOcG5HMzEtMVhKSjFZSHFuNzdBeWtPYWFYVExBIIEC; bili_jct=ae07c1fc749f3437958ac1cd54e34e37; sid=q24qtqbh; b_lsid=76C4775C_18E60BF6E75; bp_video_offset_261766594=911269228475056240"
}

def get_data(url):
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response
    raise Exception('数据请求失败~')

def parse_data(data):
    data = data.json()
    up_names = jsonpath(data,'$..name')
    titles = jsonpath(data,'$..title')
    views = jsonpath(data,'$..view')
    danmakus = jsonpath(data,'$..danmaku')
    bvids = jsonpath(data,'$..bvid')
    for name,tit,view,danmu,vid in zip(up_names,titles,views,danmakus,bvids):
        print(tit)
        print(name)
        print("播放量"+str(view))
        print("评论量"+str(danmu))
        print(vid)
        print('---'*30)

if __name__ == '__main__':
    for i in range(1,11):
        print(f'正在抓取第{i}页')
        data = get_data(url.format(i))
        parse_data(data)