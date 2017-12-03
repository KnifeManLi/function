# coding:utf-8

import time
import random

class OperAte():
    """内置函数:list.的各种操作举例.类"""
    def __init__(self, list_=[1,2,3]):
        self.title()
        self.lis = list_
        self.name = None
        self.main()

    def main(self):
        """主函数"""
        self.append()
        print('正在打印票据..请稍等')
        print('')
        self.time_()
        self.enumerate()# 调用 enumerate 方法来查找这个名字的位置
        print('请您收好.票据.里面请..')
        print("*"*30)
        print('    你好:能查下.我女朋友的电影票位置吗')
        print(" ")
        print('好的:请稍等...')
        self.time_(5)# 延迟时间
        self.count_('女朋友')# 查找指定位置
        print('')
        print('你好:我们是阳光小学的.来这里买团票')
        print('好的.将要观看电影的人.名字说下..')
        self.printf()
        self.time_()
        self.extend_()# 添加一个 list
        print('')
        baifeng = '你好:请帮我查下.白凤.的位置'
        print(baifeng)
        self.time_()
        self.index_(baifeng[9:11])
        print("")
        print('电影还有 10 分钟开始...')
        self.pop_()
        print('')
        num = random.randint(5,10)
        print('你好:请问有靠前排观看的位置吗')
        self.insert_()
        print('')
        print('你好:今天有点急事.不能开这场电影了.请将我的电影票退了.')
        print('')
        print('好的:请稍等...')
        self.time_()
        self.remove_()
        print('')
        print('小丽,将今天的销票数量整理下.拿给我.')
        print('好的:老板')
        self.sort_()# 进行排序

    def insert_(self):
        """插入到指定位置"""
        print('我给您看下..')
        self.time_()
        number = random.randint(5,50)
        print('您看:' + str(number) + '位置可以吗')
        print('')
        print('要是可以.请输入您的姓名')
        name = self.input_()
        if name != '':
            self.lis.insert(number, name)
            print('您的姓名为:.' + str(name) + '.座位在.' + str(self.lis.index(name)) + '.上面')
            print('您里面请')
        else:
            print('是感觉座位靠后了吗..您如果不满意.哪给您安排靠右边前排的吧')
            name = self.input_()
            self.lis.insert(27, name)
            print('您的姓名为:.' + str(name) + '.座位在.' + str(self.lis.index(name)) + '.上面')
            print('您里面请')

    def append(self):
        """向 list 里面添加值"""
        name = input('请输入你的名字:>>>')
        while True:
            if name != ' ':
                print('东方电影院欢迎 %s 到来' % (name))
                self.name = name
                self.lis.append(name)
                break
            else:
                print('您的名字:不能为空..')
                name = input('请输入你的名字:>>>')

    def sort_(self):
        """重大到小排序列表"""
        self.lis = self.change()
        self.lis.sort()
        print('*****'*5)
        for i, name in enumerate(self.lis, start=1):
            print('[' + str(i) + ']'+ '--' + str(name) + "--|")
        print('销票姓名如上: 人数是: %s' %(self.len_()))

    def len_(self):
        """统计人数"""
        human_number = 0
        for item in self.lis:
            human_number += 1

        return human_number

    def remove_(self):
        """删除一个电影票名字"""
        name = input('请输入你的名字:>>>')
        if name in self.lis:
            self.lis.remove(name)
            print('姓名:' + name + '.以成功退票.欢迎您有时间来看电影')
        else:
            print('您未购买电影票.请检查是否是.东方电影院.')

    def pop_(self):
        """弹出列表里面的元素"""
        if self.judeg():
            random.shuffle(self.lis)
            item = self.lis.pop()# 弹出一个值来
            print(' %s .贵宾在 %s 时间离开了' %(item, time.ctime()[11:19]))
        else:
            print('服务员:今天电影院好冷清啊,来看电影的人都没有')

    def index_(self, baifeng):
        """查找位置"""
        self.count_(baifeng, False)

    def extend_(self):
        """将购买电影票团体添加到 list 里面去"""
        if isinstance(self.box(), (list, tuple, set, str)):
            self.lis.extend(self.box())
            print('您的票以打印好.里面请...')
        else:
            print('一人无法购买团体票..')

    def count_(self, woman_name, temp=True, name='女朋友'):
        """查找指定位置"""
        if temp:
            woman_name = input('请输入你'+name+'的名字:>>>')
        if woman_name in self.lis:
            num = self.lis.count(woman_name)
            if temp:
                if num:
                    print('你好:你的女朋友在: %s 号位置上面' %(self.position))
                else:
                    print('你的女朋友还没有来.请在这里稍等片刻..')
            else:
                if num:
                    try:
                        print('你好:你的.' + woman_name + '.在: %s 号位置上面' % (self.lis.index(woman_name)))
                    except Exception:
                        print('你的' + woman_name + '不在购票中.请您确认名字..')
                else:
                    print('你的'+woman_name+'不在购票中.请您确认名字..')
        else:
            if temp:
                print('你的女朋友还没有来.请在这里稍等片刻..')
            else:
                print('你的'+woman_name+'不在购票中.请您确认名字..')

    def enumerate(self):
        """查找位置"""
        for index, item in enumerate(self.lis):
            if item == self.name:
                self.position = index
                print('你好:你的位置在第 %s 上面,名字叫 %s .' %(index, item))

    def change(self):
        """将列表的值全部转换成字符串"""
        new_list = []
        for item in self.lis:
            new_list.append(str(item))

        return new_list

    def judeg(self):
        """判断列表是否为空"""
        number = 0
        for item in self.lis:
            if 1 is number:
                break
            number += 1
        return number

    def printf(self):
        """输出"""
        print("")
        for item in self.box():
            print(item, end='.')
        print('')
        print("购买团票的人数为:", len(self.box()))
        print('*********************************')

    def box(self):
        """存放购买团票的同学名字"""
        return ['剑圣', '韦庄', '白凤', '黑麒麟', '盗圣', '张良', '蒙恬', '秃鹫']

    def time_(self, end=10):
        """延缓时间"""
        for i in range(end, 0, -1):
            print('请稍等' + "..." + str(i))
            time.sleep(1)

    def title(self):
        """方法:输出标题"""
        print('*'*20)
        print(' 欢迎来到东方电影院')
        print("*"*20)

    def input_(self):
        """输入一个名字"""
        return input('请输入您的姓名:>>>')

if __name__ == "__main__":
    OperAte()