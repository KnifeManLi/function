# coding:utf-8

import sys

class Factory(object):
    """元祖的内置函数的使用"""
    def __init__(self):
        self.i = 0# 用来记录个数
        self.null_tuple = ()
        self.main()

    def main(self):
        """主函数"""
        self.printf()
        self.index_()
        self.count_()
        self.del_()
        self.len_()
        self.max_()
        self.min_()
        self.sizeof_()

    def sizeof_(self):
        """求水果的占地面积"""
        if not(self.null_tuple):
            print('当前水果占地面积为: %s.平方' %(self.chest().__sizeof__()))# 执行没有删除出前的.水果占地面积
        else:
            print('当前水果占地面积为: %s.平方' %(self.null_tuple.__sizeof__()))# 执行删除后的.水果占地面积

    def max_(self):
        """求水果的箱最大者"""
        if not(self.null_tuple):
            print('当前最大的箱数是: %s.' %(max(self.chest())))# 执行没有删除出前的.将最大者挑出来
        else:
            print('当前最大的箱数是: %s.' %(max(self.null_tuple)))# 执行删除后的.将最大者挑出来

    def min_(self):
        """求水果的箱最大者"""
        if not(self.null_tuple):
            print('当前最小的箱数是: %s.' %(min(self.chest())))# 执行没有删除出前的.将最小者挑出来
        else:
            print('当前最小的箱数是: %s.' %(min(self.null_tuple)))# 执行删除后的.将最小者挑出来

    def del_(self):
        """删除某项水果"""
        self.len_()
        print('')
        print('请输入你要删除水果的名字,')
        print("")
        self.index_(False)
        new_tuple = list(self.chest())# 将元祖转换成列表进行莫个水果的删除
        del new_tuple[self.there]
        print("--." + self.name + ".--水果以删除掉." + "当前剩余--." + str(len(new_tuple)) + '.--箱水果')
        self.null_tuple = tuple(new_tuple)# 将剩余的水果赋给一个全局的参数
        self.chest(tuple(new_tuple), False)
        self.i += 1

    def len_(self):
        """求水果的个数"""
        print('当前水果的个数为: %s 箱' %(len(self.chest())-self.i))

    def index_(self, temp=True):
        """查找莫个水果的位置"""
        print('请输入你要查找的水果名字:..')
        self.name = self.input_()
        try:
            self.there = self.chest().index(self.name)
            if temp:
                print('您查找的水果 %s 在 %s 位置上面' %(self.name, self.there))
        except ValueError:
            print('您还没有购买这个品种的水果.请先进行购买')
            sys.exit()

    def count_(self):
        """查找莫一个水果的箱数"""
        print('请输入你要查找水果的箱数的.水果名..')
        name = self.input_()
        position = self.chest().count(name)
        if position:
            print('您查找的 %s 个数为 %s 箱.' %(name, position))
        else:
            print('您还没有购买这个品种的水果.请先进行购买')

    def input_(self):
        """输入函数"""
        return input('请输入>>>>')

    def chest(self, box=None, temp=True):
        """用来存放水果"""
        if temp:
            return ('苹果', '苹果', '苹果' '梨','葡萄','红提','枣','柑橘','柚','桃','西瓜','杏',
                '甜瓜','香瓜','荔枝','甘蔗','柿','柠檬','芒果','菠萝','桑葚','荸荠','柚子','香瓜','荔枝','甘蔗','柿','柠檬','芒果','菠萝')
        else:
            box_tuple = ('苹果', '苹果', '苹果' '梨','葡萄','红提','枣','柑橘','柚','桃','西瓜','杏',
                '甜瓜','香瓜','荔枝','甘蔗','柿','柠檬','芒果','菠萝','桑葚','荸荠','柚子','香瓜','荔枝','甘蔗','柿','柠檬','芒果','菠萝')
            box_tuple = box
            return box_tuple

    def printf(self):
        """输出标题"""
        print('*'*30)
        print('*******订购水果清单***********')
        print('*'*30)

if __name__ == "__main__":
    Factory()