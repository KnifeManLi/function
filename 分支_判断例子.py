# coding:utf-8

def seek():
    """再次请求输入的函数"""
    name = input('请输入一个名字.....')
    judeg(name, False)

def finish(number):
    """结束函数"""
    if number:
        print('7个小矮人: 公主可找到你啦.啦.啦.啦.啦.啦.啦.')
    else:
        print('老巫婆:白雪公主.去死吧..我将变成天下第一的美    人...哈哈。')

def judeg(name=None, temp=True):
    """判断函数"""
    if temp:
        name = input('请输入一个名字.....')

    if name == '白雪公主':
        print('')
        print('请上帝保佑.我的子民.和泰安康.国运昌盛')
        finish(True)
    elif name == '老巫婆':
        print('')
        print('老巫婆:告诉我.谁是天下最美丽的女人.')
        print('镜子:当然是.白雪公主了.')
        print('老巫婆:该死的.我要将白雪公主的容貌.给毁了')
        finish(False)
    else:
        print("")
        print('上帝听见请求.赐上帝的 7 个儿子去保护白雪公主')
        print(' 7 个人一起下到凡间来寻找白雪公主..')
        seek()

if __name__ == "__main__":
    judeg()

