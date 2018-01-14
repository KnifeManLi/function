# coding:utf-8

from random import shuffle

class People(object):
    """人类"""
    def __init__(self, name):
        self.name = name
        self.cage_list = []

    def __str__(self):
        if len(self.cage_list):
            return '%s:以射_%s_大雕' %(self.name, len(self.cage_list))
        else:
            return '%s:还没有射中大雕.继续努力...' %(self.name)


    def tianjia_jian(self, gong, jian):
        """"""
        gong.append_(jian)

    def she_jian(self, gong, niao, guojing):
        """"""
        jian = gong.launch()
        if jian is not None:
            jian[0].fa_she(niao, jian[1], guojing)
        else:
            print('箭以射空.无法射箭.')

class Longlow(object):
    """弓类"""
    def __init__(self, longlow='上古神弓'):
        self.longlow = longlow
        self.longlow_list = []
        self.number = [i for i in range(1, 21) if i % 2 == 0]

    def __str__(self):
        if len(self.longlow_list):
            return '箭已在:%s_上面.请进行拉弓, 箭的数量为:%s_' %(self.longlow, len(self.longlow_list))
        else:
            return '%s:上面没有箭.请去那箭' %(self.longlow)

    def launch(self):
        """"""
        if len(self.longlow_list) > 0:
            return self.longlow_list.pop()
        else:
            return None

    def num(self, jian):
        """"""
        shuffle(self.number)
        tuple_item = self.number.pop()

        return jian, tuple_item

    def append_(self, jian):
        """"""
        if len(self.longlow_list) < 10:
            number = self.num(jian)
            self.longlow_list.append(number)
        else:
            print('箭以在弓上.无法上箭')

class Sword(object):
    """剑类"""
    def __init__(self, shashangli):
        self.shashangli = shashangli

    def fa_she(self, niao, number_shashangli, guojing):
        """"""
        niao.she_zhong(number_shashangli, guojing)


class Bird(object):
    """鸟类"""
    def __init__(self, dadiao):
        self.dadiao = dadiao
        self.xieliang = [i for i in range(1,11)]

    def pop(self):
        """"""
        shuffle(self.xieliang)
        return self.xieliang.pop()

    def she_zhong(self, number_shashangli, guojing):
        """"""
        xie_liang = self.pop()
        if number_shashangli % xie_liang == 0:
            print('大雕已被:_%s_射中' %(guojing.name))
            guojing.cage_list.append('True')
        else:
            print('大雕未被:_%s_射中.大雕还剩_%s_滴血' %(guojing.name, abs(number_shashangli-xie_liang)))

def main():
    """主函数"""
    guojin = People('郭靖')
    gong = Longlow()

    for i in range(5):
        jian = Sword(10)
        guojin.tianjia_jian(gong, jian)

    print(gong)
    niao = Bird('大雕')

    guojin.she_jian(gong, niao, guojin)
    guojin.she_jian(gong, niao, guojin)
    guojin.she_jian(gong, niao, guojin)
    guojin.she_jian(gong, niao, guojin)
    guojin.she_jian(gong, niao, guojin)

    print(guojin)

if __name__ == "__main__":
    main()