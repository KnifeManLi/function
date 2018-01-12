# coding:utf-8

import random

class People(object):
    """人类"""
    def __init__(self, name):
        self.name = name
        self.blood = 100
        self.gun = None

    def push_down(self, clip, cartridge):
        """安装子弹"""
        clip.push(cartridge)

    def push_clip(self, ak, clip):
        """安装弹夹"""
        ak.push(clip)

    def a_gun(self, ak):
        """拿枪"""
        if self.gun is not None:
            print('%s:已在手中.可以开枪了')
        else:
            self.gun = ak

    def shoot(self, qinhui):
        """开枪"""
        self.gun.shoot_(qinhui)

    def loss_(self, lethality):
        self.blood -= lethality
        if self.blood > 0:
            print('%s:还剩余_%s_' %(self.name, self.blood))
        else:
            print('%s:已经死亡,哈哈')

class Clip(object):
    """弹夹类"""
    def __init__(self, number):
        self.clip_number = number
        self.clip_number_list = []

    def __str__(self):
        return "弹夹容量为:%s, 里面子弹为:%s." %(self.clip_number, len(self.clip_number_list))

    def push(self, cartridge):
        """安装子弹"""
        if len(self.clip_number_list) < self.clip_number:
            self.clip_number_list.append(cartridge)
        else:
            print('子弹已满,无法安装.请换弹夹')

    def pop(self):
        """弹出子弹"""
        if len(self.clip_number_list) > 0:
            return self.clip_number_list.pop()
        else:
            return None

class Cartridge(object):
    """子弹类"""
    def __init__(self, shashangli):
        self.lethality = shashangli

    def loss(self, qinhui):
        """掉血"""
        qinhui.loss_(self.lethality)

class Gun(object):
    """枪类"""
    def __init__(self, qiang):
        self.spear = qiang
        self.clip = None

    def __str__(self):
        if self.clip is not None:
            return '%s:已在手中...' %(self.spear)
        else:
            return '枪以丢失.手中无枪..哈哈,'

    def push(self, clip):
        """安装弹夹"""
        if self.clip is not None:
            print('枪里面已有弹夹.可以开抢了')
        else:
            self.clip = clip

    def shoot_(self, qinhui):
        """开枪"""
        car = self.clip.pop()
        if car is not None:
            car.loss(qinhui)
        else:
            print('弹夹里面没有子弹了.请安装子弹')

def main():
    """主函数"""
    yuefei = People('岳飞')
    clip = Clip(10)
    for i in range(random.randint(5,9)):
        cartridge = Cartridge(30)
        yuefei.push_down(clip, cartridge)

    print(clip)
    ak = Gun('ak47')
    yuefei.push_clip(ak, clip)
    print(ak)

    yuefei.a_gun(ak)
    qinhui = People('秦桧')
    for i in range(random.randint(2,11)):
        yuefei.shoot(qinhui)

if __name__ == "__main__":
    main()

