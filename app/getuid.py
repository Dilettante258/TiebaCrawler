from requests_html import HTMLSession
import sys, datetime
import pandas as pd


header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,en-GB;q=0.6",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61",
}

# 利用网页得到id
def getuid(url):
    session = HTMLSession()
    r = session.get(url, headers=header)
    r.html.render(sleep=2)
    if "tieba.baidu.com/home/main" in url:
        spam = r.html.find("body > script:nth-child(29)")
        spam = spam[0].text
        print('通过主页查找id')
        return spam[40:-4]
    elif 'tieba.baidu.com/p/' in url:
        spam = r.html.xpath('//*[@id="j_p_postlist"]/div[1]/div[1]/ul/li[1]/div/a/img')
        print('通过帖子查找id')
        return spam[0].attrs.get("username", None)
    elif 'tb.1.' in url:
        print('通过可能不支持的有关网页查找id，可能会导致致命错误')
        return str(getuid(f"https://tieba.baidu.com/home/main?ie=utf-8&id={url[url.find('tb.1.'):]}"))
    else:
        print("ID查找失败")
        return str(url)


if 'baidu' in sys.argv[1] or 'tb.1.' in sys.argv[1]:
    uid = getuid(sys.argv[1])
else:
    uid = sys.argv[1]


data = {'IP': [sys.argv[2]], 'UID': [uid], 'Time': [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")], 'Form Data': [sys.argv[1]]}
df = pd.DataFrame(data)
df.to_csv('./cache/IP_log.csv', index=False, header=True, mode='a+')
