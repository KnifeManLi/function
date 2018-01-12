# coding:utf-8

import random
import sys

def people(name='老王'):
    """"""
    return name

def danjia(ronglinag=10):
    """"""
    return ronglinag

def zidan(shashangli=10):
    """"""
    return shashangli

def gun(qiang='ak47'):
    """"""
    return qiang

def tanchuzidan(danjia):
    """"""
    if len(rongliang_list) < danjia:
        try:
            return rongliang_list.pop()
        except:
            print('没有子弹了.请安装子弹!!!')
            sys.exit()
    else:
        return None

def diaoxie(name, number):
    """"""
    global xieliang
    xieliang -= number
    if xieliang > 0:
        print('%s:还剩_%s_滴血.' %(name, xieliang))
    else:
        print('%s:挂了.哈哈' %(name,))

def anqiang(danjia):
    """"""
    laowang = people()
    print('抢手为:%s, 血量为:%s' %(laowang, xieliang))
    global num
    for i in range(12):
        number = tanchuzidan(danjia)
        if  number is not None:
            name = people('老赵')
            print('%s:上场了,血量为:%s_' %(name, xieliang))
            diaoxie(name, number)
        else:
            print('没有子弹了.请安装子弹')
            break

def main():
    """"""
    danjia_num = danjia()
    if len(rongliang_list) < danjia_num:
        for i in range(num):
            rongliang_list.append(zidan())

    print('弹夹为:%s.里面子弹为:%s' %(danjia_num, len(rongliang_list)))
    print('%s:已在手中' %(gun()))
    anqiang(danjia_num)

if __name__ == "__main__":
    xieliang = 100
    num = random.randint(5,9)
    rongliang_list = []
    main()