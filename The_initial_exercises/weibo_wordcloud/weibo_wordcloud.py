import requests
import wordcloud
import jieba
from scipy.misc import imread
import re

headers = {
    "Host": "m.weibo.cn",
    "Referer": "https://m.weibo.cn/u/3764300337",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) "
                  "Version/9.0 Mobile/13B143 Safari/601.1",
}

params = {"uid": "{uid}",
          # "luicode": "20000174",
          # "featurecode": "20000320",
          "type": "uid",
          "value": "3764300337",
          "containerid": "{containerid}",
          "page": "{page}"}

url ='https://m.weibo.cn/api/container/getIndex'


def clean_html(raw_html):
    pattern = re.compile(r'<.*?>|转发微博|//:|Repost|，|？|。|、|分享图片|回复@.*?:|//@.*')
    text = re.sub(pattern, '', raw_html)
    return text


def fetch_data(uid=None, container_id=None):
    """
    抓取数据，并保存到CSV文件中
    :return:
    """
    page = 0
    total = 110
    blogs = []
    for i in range(0, total//10):
        params['uid'] = uid
        params['page'] = str(page)
        params['containerid'] = container_id
        res = requests.get(url, params=params, headers=headers)
        cards = res.json().get("data").get("cards")
        # print(cards)

        for card in cards:
            # 每条微博的内容
            if card.get('card_type') == 9:
                text = card.get('mblog').get('text')
                text = clean_html(text)
                blogs.append(text)
        page += 1
        print('抓取第{page}页，目前总共抓取了{count}条微博'.format(page=page, count=len(blogs)))
    with open('weibo.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(blogs))


def draw_wordcloud():
    with open('weibo.txt', 'r', encoding='utf-8') as f:
        t = f.read()
    ls = jieba.lcut(t)
    txt = ' '.join(ls)
    mask_img = imread('python.png')
    # 不在词云中显示的词语
    word_no_show = ['第一次', '打卡', '一个', '一直', '今天', '就是', '哈哈', '一下', '不行', '他们','起床', '不错', '可以', '最后', '今日', '这道', '明早', '没有', '完成', '网易', '一起', '冻得', '分享', '希望', '现在', '感觉', '一根']
    # print(txt)
    w = wordcloud.WordCloud(
        # 指定字体为微软雅黑
        font_path = 'fzyh.ttf',
	background_color='white',
        # 指定最大显示词数和图片样式
        max_words=80, 
	stopwords = word_no_show,
        max_font_size = 60,
        mask=mask_img,
	random_state = 30
                            )
    w = w.generate(txt)
    w.to_file('weibo.png')




def main():
    fetch_data('3764300337', '1076033764300337')
    draw_wordcloud()

main()