# coding:utf-8

import time
import sys

def box():
    """这个函数用来返回.年.月.日"""
    return ['年', '月', '日', '时', '分', '秒']

def printf(list_):
    """输出当前的时间"""
    n = 0
    print('\n')
    while n < len(list_):
        if 5 is n:
            print(list_[n])# 将最后一个 - 去掉输出
        else:
            print(list_[n], end='-')
        n += 1

def judeg(value):
    """判断是否为真的函数"""
    if value:
        return True
    return False

def time_():
    """用 while 循环输出当前时间的函数"""
    tim = input('请输入一个字符串.....')
    list_ = []
    temp = True

    while temp:
        while tim == '时间':
            before = time.localtime()# 获取当前时间
            i = 0
            while i < len(before)-3:
                item = before[i]# 获取每个 年 月 日 时 分 秒 的值
                list_.append(str(item) + box()[i])#  将时间和字符串累加
                i += 1

            if judeg(list_):# 判断列表里面是否有值
                printf(list_)# 输出当前时间
                temp = False
                break# break. 跳出循环
            else:
                continue# continune.结束本次循环.继续下次的循环.不会跳出循环体

        if temp:
            print('输入错误啦.没有比配得到.换一个试试啦..')
            tim = input('请输入一个字符串.....')# 循环输入
        else:
            print('珍惜时间.关爱生命.')
            sys.exit()# 退出程序

if __name__ == "__main__":
    time_()