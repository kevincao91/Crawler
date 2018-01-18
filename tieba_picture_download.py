import requests
from bs4 import BeautifulSoup
import time
from crawlerfortieba import CrawlerForTieBas

DOWNLOAD_URL = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E6%83%85%E4%BE%A3%E5%A4%B4%E5%83%8F'
info_file = 'img_info.txt'
img_url_list = []


def save_img(content, filename):
    save_path = os.path.join('/data/t66y', filename[:4])
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    file_path = os.path.join(save_path, filename)
    with open(file_path, 'wb') as fp:
        fp.write(content)


def main():
    number_page = 1
    now_page = 0
    target_url = DOWNLOAD_URL
    #  抓取页面图片链接
    while (target_url != "") & (now_page < number_page):
        now_page += 1
        print('page ' + str(now_page) + '>>>')
        crawler = CrawlerForTieBas(target_url)
        crawler.get_info()
        img_url_list.append(crawler.img_url_list)

        info_file = 'img_url.txt'
        with open(info_file, 'w') as file_object:
            for img_url in img_url_list:
                file_object.write(img_url)

    #  保存图片
    for img_url in img_url_list:
        pass
    print('All Done!')


if __name__ == '__main__':
    main()
