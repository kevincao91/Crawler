import requests
from bs4 import BeautifulSoup
import time


class CrawlerForTieBas():
    #  表示单个贴吧爬虫的类
    def __init__(self, target_url):
        self.target_url = target_url
        self.post_url_list = []
        self.next_pag = target_url
        self.start_time = time.time()
        self.finish_time = time.time()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/47.0.2526.80 Safari/537.36 '}

    def download_page(self):
        #  html = requests.get(self.target_url, headers=self.headers).content
        html = requests.get(self.target_url).content
        return html

    def parse_html(self, html):
        soup = BeautifulSoup(html)
        #  查找页面中所有post的URL
        post_list_soup = soup.find_all('a', attrs={'class': 'j_th_tit '})
        for post_soup in post_list_soup:
            if post_soup:
                post_url = 'https://tieba.baidu.com' + post_soup.get('href')
                self.post_url_list.append(post_url)
        #  查找下一页URL
        next_pag_soup = soup.find('a', text={'下一页>'})
        if next_pag_soup:
            self.next_pag = 'https:' + next_pag_soup.get('href')
        else:
            self.next_pag = ""

    def get_info(self):
        if self.target_url:
            html = self.download_page()
            self.parse_html(html)
            self.finish_time = time.time()
