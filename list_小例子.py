# coding:utf-8

import time
import sys
from random import shuffle

def box():
    """函数"""
    return ["大象", "老鼠", '犀牛']

def printf(animin_list, name=None):
    """输出函数"""
    print(name)
    i = 0
    for item in animin_list:
        if len(animin_list) - 1 is i:
            print(item, end='')
        else:
            print(item, end='-')
        i += 1
    print('')

def be_away(animin_list):
    """离开函数：没有调用"""
    shuffle(animin_list)
    leave = animin_list.pop()
    print('')
    print(' %s 先生在 %s 离开' % (leave, time.ctime()))
    print('')

def main():
    """主函数"""
    print("*" * 30)
    print('   欢迎来到:动物世界大会..')
    print("*"*30)
    animin_list = box()
    printf(animin_list, "目前:主持人都有")

    n = 1
    name = input('请输入您的入场名是:>>>')
    print('欢迎 %s 先生的到来' %(name))

    while True:
        if name not in animin_list:
            animin_list.append(name)# 用 append 内置函数将新到来的人添加到列表里面去
            printf(animin_list, '目前嘉宾都有:')
        else:
            print('')
            print('%s 先生已经到来..' %(name))
            print('请您回去吧...<哈.哈>')
            for i in range(1,6):
                print('叮.咚'*i)
                time.sleep(1)
            print('有请下一位.')

        if 30 is n:
            print(" -----------------")
            print('|-动物大会正式开始-|')
            print(" -----------------")
            printf(animin_list, '到场嘉宾都有:')
            print("人数为:%s 个" %(len(animin_list)))
            sys.exit()

        print('')
        name = input('请再次输入您的入场名是/输入:0:结束:>>>')
        n += 1
        print('')
        if name.isnumeric():# 判断是否里面全是数字
            if int(name) is 0:
                print('感谢您的到来..')
                sys.exit()# 退出程序

if __name__ == "__main__":
    main()