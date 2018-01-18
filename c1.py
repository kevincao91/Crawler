import requests
from bs4 import BeautifulSoup
import json

DOWNLOAD_URL = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E6%83%85%E4%BE%A3%E5%A4%B4%E5%83%8F'


def parse_html(html):
    soup = BeautifulSoup(html)
    img_url_list = []
    floor_list_soup = soup.find_all('div', attrs={'class': 'threadlist_detail clearfix'})
    for floor_soup in floor_list_soup:
        floor_content_soup = floor_soup.find('ul', attrs={'class': 'threadlist_media j_threadlist_media clearfix'})
        if floor_content_soup:
            content_li_list = floor_content_soup.find_all('li')
            if content_li_list:
                for content_li in content_li_list:
                    img_detail = content_li.find('img')
                    print(img_detail.get('bpic'))
    return img_url_list


def download_page(url):
    html = requests.get(url).content
    return html


def main():
    do_url = DOWNLOAD_URL
    info_file = 'temp.json'
    with open(info_file, 'w') as file_object:
        while do_url:
            html = download_page(do_url)
            img_url_list = parse_html(html)
            json.dump(img_url_list, file_object)
            do_url = False
    print('Done!')


if __name__ == '__main__':
    main()
