# coding:utf-8

import time

def box():
    """这个函数返回一个列表"""
    return ['年', '月', '日', '时', '分', '秒']

def function():
    """这个函数输出一个今年的.年-月-日."""
    t_list = time.localtime()# 输出当前的时间
    li = []
    for index in range(6):
        s1 = t_list[index]# 用下标的方式获取值
        li.append(str(s1)+box()[index])# 例 2017 + 年, 11 + 月......

    for i,item in enumerate(li):
        if 5 is i:# 将最后一个 横杠去掉
            print(item, end='')
        else:
            print(item,end='-')
        time.sleep(0.5)

def bracktes():
    """返回一个 小括号. 用来做函数的调用"""
    return '()'

def wrong():
    """提示一个错误信息"""
    print('没有这个函数.请重新输入.')
    sun_str = input('请输入一个函数的名字.要以字符串的形式.比如:"func":>>>')
    main(sun_str, False)#


def string():
    """返回一个提示信息"""
    return '请输入 function 或 function()'

def main(sun_str=None, temp=True):
    """主函数"""
    if temp:
        sun_str = input('请输入一个函数的名字.要以字符串的形式.比如:"func":>>>')

    if 8 is len(sun_str):
        new_str = sun_str + bracktes()# 将其拼接成一个函数
        eval(new_str)# 将字符串进行解析. 进行函数的调用
    elif 10 is len(sun_str):
        eval(sun_str)# 将字符串解析成一个函数.
    else:
        wrong()# 函数的循环调用.知道输入对的函数名字 退出

if __name__ == "__main__":
    main()
