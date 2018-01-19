import os
import time
from skimage import io



DOWNLOAD_URL = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E6%83%85%E4%BE%A3%E5%A4%B4%E5%83%8F'
info_file = 'img_url.txt'
save_path = 'images/'
img_url_list = []


def save_img(img_url, filename):
    file_path = save_path + filename
    try:
        image = io.imread(img_url)
    except OSError:
        print('【错误】当前图片无法下载')
    try:
        io.imsave(file_path, image)
    except UnboundLocalError:
        print('【错误】当前图片无法下载')


def save_img_list(img_url_list):
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    index = 0
    for img_url in img_url_list:
        filename = str(index) + img_url[-5:-1]
        print(index)
        save_img(img_url[:-1], filename)
        index += 1


def main():
    number_page = 1
    now_page = 0
    img_url_list = []
    target_url = DOWNLOAD_URL
    #  抓取页面图片链接
    while (target_url != "") & (now_page < number_page):
        now_page += 1
        print('page ' + str(now_page) + '>>>')

        '''
        crawler = CrawlerForTieBas(target_url)
        crawler.get_info()
        img_url_list += crawler.img_url_list
        #  保存图片URL
        save_start_time = time.time()
        with open(info_file, 'w') as file_object:
            for img_url in img_url_list:
                file_object.writelines(img_url + '\n') 
        '''

        #  读取URL文件
        save_start_time = time.time()
        with open(os.path.realpath(info_file)) as file_object:
            img_url_list = file_object.readlines()  # 读取全部内容
        #  保存图片
        save_img_list(img_url_list)
        save_end_time = time.time()
        print('Save has been done! in ' + str(save_end_time - save_start_time) + 's')
    print('All Done!')


if __name__ == '__main__':
    main()
