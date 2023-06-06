import threading
from ctypes import windll
import time
import random


class DDkey:
    def __init__(self, k=None, d_k=None):
        """
        :param k:  按住的键 只能一个
        :param d_k:  需要连击的键  ,可以是多键位 字符串格式 ,使用逗号隔
        """
        try:
            self.dd = windll.LoadLibrary(r"E:\Py\catwu\DD94687.64.dll")
            self.st = self.dd.DD_btn(0)  # 初始化
            self.examine()
        except OSError:
            print('请使用管理员身份运行程序')

        # DD虚拟码，可以用DD内置函数转换。
        self.vk = {'5': 205, 'c': 503, 'n': 506, 'z': 501, '3': 203, '1': 201, 'd': 403, '0': 210, 'l': 409, '8': 208,
                   'w': 302,
                   'u': 307, '4': 204, 'e': 303, '[': 311, 'f': 404, 'y': 306, 'x': 502, 'g': 405, 'v': 504, 'r': 304,
                   'i': 308,
                   'a': 401, 'm': 507, 'h': 406, '.': 509, ',': 508, ']': 312, '/': 510, '6': 206, '2': 202, 'b': 505,
                   'k': 408,
                   '7': 207, 'q': 301, "'": 411, '\\': 313, 'j': 407, '`': 200, '9': 209, 'p': 310, 'o': 309, 't': 305,
                   '-': 211,
                   '=': 212, 's': 402, ';': 410,
                   'f1': 101, 'f2': 102, 'f3': 103, 'f4': 104, 'f5': 105, 'f6': 106, 'f7': 107, 'f8': 108, 'f9': 109,
                   'f10': 110}

        self.k = k  # 按住的键
        self.d_k = d_k  # 需要连击的键

        # 按键延时
        self.delay_mini = 40
        self.delay_max = 85

        self.is_circulate = False  # 循环模式开关
        self.is_clicking = False
        self.key = None
        self.click_thread = None

        self.listener = None  # 键盘钩子

    def examine(self):
        if self.st != 1:
            print("错误初始化失败")
            exit(101)
        else:
            print('初始化成功')

    def dd_key(self):
        ran = random.randint(40, 85) / 1000
        for k in self.d_k:
            self.dd.DD_key(self.vk[k], 1)
            time.sleep(ran)
            self.dd.DD_key(self.vk[k], 2)

    # ---------------------------------------------------------------------
    def dd_click(self):
        """无脑循环模式"""
        while self.is_circulate:
            self.dd_key()
            e = random.randint(int(self.delay_mini), int(self.delay_max)) / 1000
            time.sleep(e)
            print(e)

    def dd_click_start(self):
        """开始无脑循环"""
        self.is_circulate = True
        self.click_thread = threading.Thread(target=self.dd_click)
        self.click_thread.daemon = True
        self.click_thread.start()

    def dd_click_stop(self):
        """停止无脑循环模式"""
        self.is_circulate = False
        self.click_thread.join()

