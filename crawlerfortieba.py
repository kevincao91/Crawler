import requests
from bs4 import BeautifulSoup
import time


class CrawlerForTieBas():
    #  表示单个贴吧爬虫的类
    def __init__(self, target_url):
        self.target_url = target_url
        self.img_url_list = []
        self.start_time = time.time()
        self.finish_time = time.time()

    def download_page(self):
        html = requests.get(self.target_url).content
        return html

    def parse_html(self, html):
        soup = BeautifulSoup(html)
        floor_list_soup = soup.find_all('div', attrs={'class': 'threadlist_detail clearfix'})
        for floor_soup in floor_list_soup:
            floor_content_soup = floor_soup.find('ul', attrs={'class': 'threadlist_media j_threadlist_media clearfix'})
            if floor_content_soup:
                content_li_list = floor_content_soup.find_all('li')
                if content_li_list:
                    for content_li in content_li_list:
                        img_detail = content_li.find('img')
                        img_url = img_detail.get('bpic')
                        self.img_url_list.append(img_url)

    def get_info(self):
        if self.target_url:
            html = self.download_page()
            self.parse_html(html)
            self.finish_time = time.time()
        print('Scan has been done! in ' + str(self.finish_time - self.start_time) + 's')
