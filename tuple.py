# coding:utf-8

import time
import sys
from random import shuffle

class Hero(object):
    """元祖的简单使用"""
    def __init__(self):
        self.printf()
        self.select()

    def select(self):
        """进行英雄的选择"""
        print('你有.3.次选择的机会.好好把握啊')
        j, k = 0, 0
        for i in range(3, 0, -1):
            print('请输入一个.整数.来选择英雄')
            try:
                number = int(input("请输入>>>>>>"))
                if number < len(self.assignment()):
                    self.name = self.zhuan_huan()[number]
                    k += 1
                    self.comparison(k)# 进行查找数据
                else:
                    new_number = number % i
                    self.name = self.zhuan_huan()[new_number]
                    j += 1
                    self.comparison(j)# 进行查找数据
            except Exception:
                for j in range(3,0,-1):
                    print('输入非法..进入倒计时..' + str(j))
                    time.sleep(1)

                if i > 2:
                    print('你有两次机会噢')
                elif i > 1:
                    print('你还有一次机会噢')
                else:
                    print('最后的机会.不用给你的.因为你是一个.笨蛋.')
                    sys.exit()# 直接退出程序

    def zhuan_huan(self):
        """将元祖转换成列表将数据进行打乱之后.再将其转换成元祖"""
        list_box = list(self.assignment())
        shuffle(list_box)
        return tuple(list_box)

    def comparison(self, t_n):
        """进行数据的比对"""
        box = ('9盖聂', '8卫庄', '6张良', '5韩非子', '3白凤凰', '2蒙田', '1少羽')
        temp = False
        for item in box:
            if item[1:] == self.name:
                temp = True
                self.get_name = item
                break
        if temp:
            self.reward()
        else:
            print('很遗憾.没有猜对.你还有-.'+ str(3-t_n) + '次机会.-好好加油噢...')

    def reward(self):
        """对查到英雄的奖励"""
        n = int(self.get_name[:1])
        print('恭喜你猜对了.' + self.get_name[1:] + '英雄.请领取奖励....')
        print('')
        for k in range(1,n+1):
            print('-奖励-.' + str(k) + ".-颗糖-")
            time.sleep(2)
        print('')
        print('这位施主.我看你骨骼奇特.一定是个练武奇才.来我有一本秘籍.要给你.书名为:<天下第一剑>,收好了')
        print('')

    def printf(self):
        """输出"""
        print('------------------------------')
        print('-------欢迎来到:英雄大会-------')
        print('******************************')
        print('****盖聂:   奖励.9.颗糖*******')
        print('****卫庄:   奖励.8. 颗糖*******')
        print('****张良:   奖励.6. 颗糖*******')
        print('****韩非子: 奖励.5. 颗糖*******')
        print('****白凤凰: 奖励.3. 颗糖*******')
        print('****蒙田:   奖励.2. 颗糖*******')
        print('****少羽:   奖励.1. 颗糖*******')
        print('******************************')
        print('')
        print('>>>:猜对.英雄有奖励噢..')
        print('')

    def assignment(self):
        """人物"""
        return ('盖聂', '天明', '少羽', '端木蓉', '高月', '班大师', '卫庄', '赤练', '无双鬼', '苍狼王',
                '白凤凰', '梁叔', '蒙田', '范师傅', '秦王', '李斯', '张良', '韩非子', '黑鸦', '你是一头猪', '笨蛋',
                '无知', '你还一头猪', '哎.你真是.笨')

if __name__ == "__main__":
    Hero()