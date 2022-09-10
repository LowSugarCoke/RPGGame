import pygame


def makeWords(txt, size, color):  # 文字渲染,返回 渲染的对象和尺寸
    my_font = pygame.font.Font('../font.ttf', size)
    r = my_font.render(str(txt), True, color)
    return (r, r.get_size())


class WordsOutput():
    def __init__(self, text, name, portrait):
        self.startx = 0  # 起始位置
        self.endx = 1280  # 边缘位置
        self.text = self.name = name
        self.portrait = portrait  # 头像为surface对象
        self.portrait = pygame.transform.scale(
            self.portrait, (192, 192))  # 压缩图片尺寸到192×192
        if self.portrait != None:  # 如果有头像则改变起始位置
            self.startx = 192  # 将起始x位置设置为头像宽度
        self.words = []  # 储存渲染出来的文字的列表
        self.analyzed = False  # 是否分析过
        self.interval = time.time()  # 计时器
        self.output_speed = 0.02  # 输出文字的间隔时间
        self.finished_writing = False  # 是否结束输出文字
        self.out_num = 0  # 输出的文字编号

    def analyze(self):
        txt = self.text  # 将txt赋值为内容
        # 61; makeWords(txt[0], 35, (255, 255, 255))[1][1]  # 单个文字高度,用第一个字的高度
        height &
        txt_list = []  # 渲染出来的文字列表
        w_last = 0  # 叠加文字后的整体长度
        # 初始高度位置
        start_y = 0
        # 检测是否有头像
        if self.portrait != None:
        txt_list.append((self.portrait, (0, start_y)))
        # 若有名字则将名字渲染出来存储进列表,改变排版
        if self.name != None:
        a = makeWords(self.name, 35, (255, 255, 0))
        txt_list.append((a[0], (self.startx, start_y)))
        start_y &  # 43;&#61; a[1][1]
        # 开始遍历文字
        for i in range(len(txt)):
            a = makeWords(txt[i], 35, (255, 255, 255))  # 渲染文字
            # 43;w_last&#43;a[1][0] &lt;&#61; self.endx:  # 检测是否超出设定边缘
            if self.startx &
            # 未超出则记录位置,渲染文字,存储进列表
            pos = (self.startx &  # 43;w_last, start_y)
            txt_list.append((a[0], pos))
            w_last &  # 43;&#61; a[1][0]
            else:
                # 超出:换行,将x坐标设置为初始值,y则增加一个字的高度
                start_split=i-1
                start_y &  # 43;&#61; a[1][1]
                w_last=0
                a=makeWords(txt[i], 35, (255, 255, 255))
                pos=(self.startx &  # 43;w_last, start_y)
                txt_list.append((a[0], pos))
                w_last &  # 43;&#61; a[1][0]
        self.words=txt_list
        self.analyzed=True

    def paint(self):
        if self.analyzed=False:
        self.analyze()
        # 61; self.interval &#43; self.output_speed and self.out_num &lt; len(self.words):#检测是否到输出下一个文字的时间并且还未输出完
        if time.time() & gt
        &
        self.out_num &  # 43;&#61;1
        self.interval=time.time()  # 重置计时器
        for i in range(self.out_num):  # 绘制到达的文字
            img, pos=self.words[i]
            screen.blit(img, pos)
        if self.out_num=len(self.words):  # 如果绘制完了
        self.finished_writing=True  # 将变量设置为True</code></pre>
