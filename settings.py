class Settings():
    # 配置程序所有的设置数据
    def __init__(self):
        #  初始化程序的设置
        #
        # self.start_url = 'https://tieba.baidu.com/f?kw=%E5%B0%8F%E5%B0%8F%E7%BD%97&ie=utf-8'  # 小小罗吧
        # self.start_url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E6%83%85%E4%BE%A3%E5%A4%B4%E5%83%8F'  # 情侣头像吧
        self.start_url = 'https://tieba.baidu.com/f?kw=%E4%BA%8C%E6%AC%A1%E5%85%83&ie=utf-8'  # 二次元吧
        self.root_dir_name = '二次元/'
        self.save_dir_path = self.root_dir_name + 'images_' + self.start_url[27:36] + '/'
        self.post_url_list = []
        self.max_tieba_number = 1
        self.now_tieba_number = 0
        self.img_url_list = []
        self.max_pag_number = 1
        self.now_pag_number = 0
        self.download_number = 0
        self.total_s_post_num = 0
        self.total_d_pic_num = 0

    def reset(self, post_url):
        self.save_dir_path = self.root_dir_name + 'images_' + post_url[27:36] + '/'
        self.download_number = 0
        self.now_pag_number = 0

