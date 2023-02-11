import datetime
import http.client
import openpyxl
import time
from collections import Counter
from openpyxl.styles import Font, Alignment, Side, Border
from requests_html import HTMLSession
import bs4
import jieba
import jieba.analyse
import requests
from matplotlib import pyplot as plt
from wordcloud import WordCloud
import zipfile
import logging
from Configure import mnoma
import os,sys
import shutil


uid = sys.argv[1]



# 自定义变量
Vvocabulary = "哔哩哔哩 Bilibili ASOUL AS 阿畜 3u 3c 4u 4c 5u 5c v87 v8 587 487 然87 33 中之人 eoe ec 向晚 Ava 晚畜 晚醋 晚÷ 贝拉 Bella 珈乐 Carol 嘉然 Diana 然然 然比 乃琳 Eileen 乃宝 柑橘涩子 衿儿 伍敏慧 生死狙击 千袅official 顶碗人 贝极星 黄嘉琪 皇珈骑士 嘉心糖 乃琪琳 个人势 企业势 歌势 虚拟偶像 歌回 杂谈势 杂谈回 舞蹈势 舞蹈回 皮套 a÷ 鲨卵 v÷ ylg 孝孩梓 阿梓 a/ aoe 吉吉国 鬼屋 贵物 rp vtb 梁木 冲塔 推塔 挖掘机 连体人 mmr 萌萌人 ky cp民 箱推 组合推 DD yhm SC"
deleteword = "[图片]  @ (呵呵) (哈哈) (吐舌) (太开心) (笑眼) (花心) (小乖) (乖) (捂嘴笑) (滑稽) (你懂的) (不高兴) (怒) (汗) (黑线) (泪) (真棒) (喷) (惊哭) (阴险) (鄙视) (酷) (啊) (狂汗) (what) (疑问) (酸爽) (呀咩爹) (委屈) (惊讶) (睡觉) (笑尿) (挖鼻) (吐) (犀利) (小红脸) (懒得理) (勉强) (突然兴奋) (黑头高兴) (欢呼) (嘿嘿嘿) (微微一笑) (吃瓜) (托腮) (摊手) (困成狗) (暗中观察) (柯基暗中观察) (喝酒) (噗) (紧张) (炸药) (黑头瞪眼)"


# 服务器http协议1.0,指定客户端http协议版本,防止报错
http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'


# 二分法猜测结束页,125行现测试单线程改为10
def guess_max(low: int, high: int, uid) -> int:
    url = requests.get(f'https://www.82cat.com/tieba/reply/{uid}/{high}')
    if not bs4.BeautifulSoup(url.text, "html.parser").select('.alert.alert-warning.show'):
        return high
    while low <= high:
        mid = (low + high) // 2
        url = requests.get(f'https://www.82cat.com/tieba/reply/{uid}/{mid}')
        if bs4.BeautifulSoup(url.text, "html.parser").select('.alert.alert-warning.show'):
            high = mid - 1
        else:
            low = mid
    logging.info(f"Got it, the ultimate page is page {low}.")
    return low


# 拆分循环避免列表溢出
countall = Counter()
balist = []
commentlist = []
datelist = []
Comments = []
other_dict = {}
Class_Comments = []


class Comment:
    def __init__(self, ba, comment, date):
        self.ba = ba
        self.comment = comment
        self.date = date


def process_interval(st, en, uid):
    global balist
    global commentlist
    global datelist
    global countall
    global Comments
    global Class_Comments
    for i in range(st, en + 1):
        time.sleep(0.06)
        requests.adapters.DEFAULT_RETRIES = 5
        while True:
            try:
                print(f'https://www.82cat.com/tieba/reply/{uid}/{i}')
                res = requests.get(f'https://www.82cat.com/tieba/reply/{uid}/{i}', timeout=(30, 50))
                break
            except:
                print("Connection refused by the server...Let me sleep for 5 seconds.")
                logging.info("Connection refused by the server...Let me sleep for 5 seconds.")
                time.sleep(5)
                logging.info("Was a nice sleep, now let me continue...")
                continue
        Soup = bs4.BeautifulSoup(res.text, "html.parser")
        elems = Soup.select('a[target="_blank"]')
        Comments = Soup.select('li[class="mb-1"]')
        dates = Soup.select('span[class="text-muted"]')
        logging.info("Getting page %d..." % i)
        for m in range(0, len(elems) - 4, 2):
            #if '沙井渣女' in elems[m].getText():
                #break
            balist.append(elems[m].getText())
        for n in range(0, len(Comments)):
            commentlist.append(Comments[n].getText())
        for o in range(0, len(dates)):
            datelist.append(datetime.datetime.strptime(dates[o].getText(), '%Y年%m月%d日 %H时%M分%S秒'))
    for v, s in enumerate(commentlist):  # 源网页代码有问题，研究了2个小时最后只能笨办法筛除
        second_colon_index = s.index('：', s.index('：') + 1)  # 找到第二个冒号的位置
        commentlist[v] = s[second_colon_index + 1:-21]  # 保留下剩余的部分
        if "回复 @" in commentlist[v]:
            commentlist[v] = commentlist[v][6:]
    for v, s in enumerate(commentlist):
        Class_Comments.append(Comment(balist[v], s, datelist[v]))
    counts = Counter(balist)
    countall += counts
    logging.info(countall)


def organizedata():
    global counts_dict
    global other_dict
    total = sum(counts_dict.values())  # 求所有值的和
    new_counts_dict = {}  # 定义一个新字典
    other_sum = 0  # 定义一个变量记录其他的和
    for key, value in counts_dict.items():  # 遍历原字典
        if value / total < 0.02:  # 如果占比在5%以下
            other_sum += value  # 将值加到other_sum中
            other_dict[key] = value  # 将对应的键值对加入到other_dict
        else:
            new_counts_dict[key] = value  # 将值加入到新字典中
    new_counts_dict['其他'] = other_sum  # 将其他的值加入到新字典中
    return new_counts_dict  # 输出新字典


def delete():
    global commentlist
    global deleteword
    deletelist = deleteword.split(' ')
    for i in range(len(commentlist)):
        for word in deletelist:
            commentlist[i] = commentlist[i].replace(word, '')


# 启动函数
def gets(uid):
    print(f'gets部分id获取成功{uid}')
    startTime = time.time()
    if not mnoma:
        range_size = guess_max(1, 1000, uid)
    else:
        pg = int(mnoma) // 30
        temp_list = [pg, guess_max(1, 20, uid)]
        range_size = min(temp_list)
    interval_size = 50
    interval_count = range_size // interval_size + (range_size % interval_size != 0)
    for k in range(interval_count):
        print(f"现在是第{k + 1}组...")
        logging.info(f"现在是第{k + 1}组...")
        start = k * interval_size + 1
        if k == interval_count - 1:
            end = range_size
        else:
            end = start + interval_size - 1
        process_interval(start, end, uid)
    endTime = time.time()
    print('Took %s seconds.' % (endTime - startTime))
    logging.info('Took %s seconds.' % (endTime - startTime))
    global counts_dict
    counts_dict = dict(countall)
    print(counts_dict)
    logging.info(counts_dict)


# 数据可视化输出
def makepiechart(uid):
    logging.info('Making the pie chart...')
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 汉字字体
    plt.rcParams['font.family'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
    keys = list(organizedata().keys())
    values = list(organizedata().values())
    plt.pie(values, labels=keys, autopct='%1.1f%%')
    plt.title("回复贴分布饼图")
    plt.savefig(f'/www/wwwroot/default/cache/{uid}/回复贴分布饼图.jpg', dpi=300, bbox_inches='tight')
    plt.clf()
    keys = list(other_dict.keys())
    values = list(other_dict.values())
    plt.pie(values, labels=keys, autopct='%1.1f%%')
    plt.title("其他回复贴分布饼图")
    plt.savefig(f'/www/wwwroot/default/cache/{uid}/其他回复贴分布饼图.jpg', dpi=300, bbox_inches='tight')
    plt.clf()


# 将一些乱七八糟的东西录入词典
def addword():
    global Vvocabulary
    global lists
    lists = Vvocabulary.split(' ')
    global balist
    for x in balist:
        lists.append(x)
    for y in lists:
        jieba.add_word(y)


# 统计词频,由于jieba库没有统计词频的功能，因此这块要额外写
def wordcount(text):
    # 文章字符串前期处理
    strl_ist = jieba.lcut(text, cut_all=True)
    count_dict = {}
    all_num = 0
    # 如果字典里有该单词则加1，否则添加入字典
    for word in strl_ist:
        if len(word) <= 1:
            continue
        else:
            all_num += 1
        if word in count_dict.keys():
            count_dict[word] = count_dict[word] + 1
        else:
            count_dict[word] = 1
    # 按照词频从高到低排列
    count_list = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    return count_list, all_num


def analyze(text_list):  # 将得到的文本的list，进行分析
    text = ""
    for t in text_list:
        text += t
    _analyze = jieba.analyse.extract_tags(text, topK=50, withWeight=False, allowPOS=())
    result_list = " ".join(_analyze).split(' ')
    count_list, all_num = wordcount(text)
    return result_list, count_list, all_num


def generate_wordcloud(title_list, article_list, uid):  # 制作词云
    title_text = ""
    article_text = ""
    for t in title_list:
        title_text += t
    for a in article_list:
        article_text += a

    wc = WordCloud(font_path="SimHei.ttf", max_words=50, background_color='white', width=800, height=500)
    title_words = " ".join(jieba.cut(title_text, cut_all=False))
    title_wordcloud = wc.generate(title_words)
    plt.imshow(title_wordcloud)
    plt.axis("off")
    plt.title('回帖分布词云')
    plt.savefig(f'/www/wwwroot/default/cache/{uid}/回帖分布词云.jpg', dpi=300, bbox_inches='tight')
    plt.clf()

    article_words = " ".join(jieba.cut(article_text, cut_all=False))
    article_wordcloud = wc.generate(article_words)
    plt.imshow(article_wordcloud)
    plt.axis("off")
    plt.title('回贴词云')
    plt.savefig(f'/www/wwwroot/default/cache/{uid}/回贴词云.jpg', dpi=300, bbox_inches='tight')
    plt.clf()


def generatewordcloud(uid):
    global commentlist
    global commenttext
    global balist
    addword()
    delete()
    commenttext = '    '.join(commentlist)
    text_word_list, text_all_num = wordcount(commenttext)
    logging.info(text_word_list[0:100])
    title_result_list, title_count_list, title_word_all_num = analyze(balist)
    text_result_list, text_count_list, text_word_all_num = analyze(commenttext)
    generate_wordcloud(title_result_list, text_result_list, uid)


# 输出数据到Excel表格中
def saveexcel(uid):
    logging.info("Saving comments...")
    wb = openpyxl.Workbook()
    sheet = wb["Sheet"]
    sheet.title = '所有评论'
    sheet['A1'] = '回帖'
    sheet['B1'] = '发布吧'
    sheet['C1'] = '时间'
    sheet.freeze_panes = 'A2'
    sheet.row_dimensions[1].height = 15.75
    listhead = [sheet["A1"], sheet["B1"], sheet["C1"]]
    fontObj1 = Font(name="SimHei", size=14, bold=True)
    side1 = Side(style="medium", color="000000")
    border = Border(left=side1, right=side1, top=side1, bottom=side1)
    for cell in listhead:
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.font = fontObj1
        cell.border = border
    sheet.column_dimensions['A'].width = 45
    sheet.column_dimensions['B'].width = 15
    sheet.column_dimensions['C'].width = 20
    for v, s in enumerate(Class_Comments):
        sheet[f'A{v + 2}'] = s.comment
        sheet[f'B{v + 2}'] = s.ba
        sheet[f'B{v + 2}'].alignment = Alignment(horizontal="center", vertical="center")
        sheet[f'C{v + 2}'] = s.date.strftime("%Y-%m-%d %H:%M:%S")
        sheet[f'C{v + 2}'].alignment = Alignment(horizontal="center", vertical="center")
    wb.save(f'/www/wwwroot/default/cache/{uid}/Comments.xlsx')


# 保存最终结果文件
def savezipfile(uid):
    newZip = zipfile.ZipFile(f'/www/wwwroot/default/cache/{uid}/结果-{uid}.zip', 'w')
    os.chdir(f'cache/{uid}')
    filelist = ['ProgramLog.txt', 'Comments.xlsx', '回复贴分布饼图.jpg', '其他回复贴分布饼图.jpg', '回帖分布词云.jpg',
                '回贴词云.jpg']
    for data in filelist:
        newZip.write(data, compress_type=zipfile.ZIP_DEFLATED)
    newZip.close()


def execute(uid):
    logging.basicConfig(filename=f'cache/{uid}/ProgramLog.txt', filemode='w+', level=logging.INFO, format=' %(asctime)s-%(levelname)s-%(message)s')
    gets(uid)
    makepiechart(uid)
    generatewordcloud(uid)
    saveexcel(uid)
    savezipfile(uid)

execute(uid)