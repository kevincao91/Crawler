import requests
from bs4 import BeautifulSoup
import time

DOWNLOAD_URL = 'https://movie.douban.com/top250'


def parse_html(html):
    soup = BeautifulSoup(html)
    movie_name_list = []
    movie_list_soup = soup.find('ol', attrs={'class': 'grid_view'})

    for movie_li in movie_list_soup.find_all('li'):
        detail = movie_li.find('div', attrs={'class': 'hd'})
        movie_name = detail.find('span', attrs={'class': 'title'}).getText()
        movie_name_list.append(movie_name)

    next_page = soup.find('span', attrs={'class': 'next'}).find('a')
    if next_page:
        return movie_name_list, DOWNLOAD_URL + next_page['href']  # 'href'超链接属性
    return movie_name_list, None


def download_page(url):
    html = requests.get(url).content
    return html


def main():
    page = 0
    do_url = DOWNLOAD_URL
    info_file = 'movie_top_250.txt'
    with open(info_file, 'w') as file_object:
        while do_url:
            page += 1
            time_start = time.time()
            html = download_page(do_url)
            movies, do_url = parse_html(html)
            file_object.write(u'{movies}\n'.format(movies='\n'.join(movies)))
            time_end = time.time()
            print('page ' + str(page) + ' finished in ' + str(time_end - time_start) + 's')
    print('Done!')


if __name__ == '__main__':
    main()
