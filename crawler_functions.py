
import requests
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'https://tieba.baidu.com/p/5469561022'


def parse_html(html):
    soup = BeautifulSoup(html)
    pic_url_list = []
    floor_list_soup = soup.find('div', attrs={'class': 'l_post l_post_bright j_l_post clearfix  '})
    print(floor_list_soup)
    for floor_soup in floor_list_soup:
        floor_content = floor_soup.find('div', attrs={'class': 'd_post_content j_d_post_content '})
        img_list_soup = floor_content.find('div', attrs={'class': 'BDE_Image'})
        img_url = img_list_soup.getText()
        pic_url_list.append(img_url)
    return pic_url_list


def download_page(url):
    html = requests.get(url).content
    return html


if __name__ == '__main__':
    html = download_page(DOWNLOAD_URL)
    print(html)
    movies, do_url = parse_html(html)
