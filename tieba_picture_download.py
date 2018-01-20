import time
import os
from settings import Settings
from crawlerfortieba import CrawlerForTieBas
import post_picture_download as post_computing


def main():
    #  设置参数 ========================================================================================================
    print('Function Start.')
    global_set = Settings()
    target_url = global_set.start_url
    if not os.path.exists(global_set.root_dir_name):
        os.mkdir(global_set.root_dir_name)
    #  创建爬虫
    crawler_tieba = CrawlerForTieBas(target_url)
    start_time = time.time()
    #  抓取页面Post链接 ================================================================================================
    while (crawler_tieba.target_url != "") & (global_set.now_tieba_number < global_set.max_tieba_number):
        #  显示开始抓取信息
        global_set.now_tieba_number += 1
        print('tieba page ' + str(global_set.now_tieba_number))
        #  抓取信息
        crawler_tieba.get_info()
        #  显示抓取结果
        print(str(len(crawler_tieba.post_url_list)) + ' posts has been find.')
        #  开始调用post爬虫抓取图片 ====================================================================================
        index_post = 0
        for post_url in crawler_tieba.post_url_list:
            index_post += 1
            print('>>> post ' + str(index_post))
            global_set.reset(post_url)
            post_computing.post_main(post_url, global_set)
            print('>>> post ' + str(index_post) + ' Done!')
            global_set.total_s_post_num += 1
    #  显示结束信息  ===================================================================================================
    end_time = time.time()
    print('Function Finished! in ' + str(end_time - start_time) + 's')
    print(str(global_set.total_s_post_num) + ' post has been scan, and ', end="")
    print(str(global_set.total_d_pic_num) + ' images has been download.')


if __name__ == '__main__':
    main()
