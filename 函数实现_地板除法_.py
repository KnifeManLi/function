# coding:utf-8

def deicde_type(f,n):
    """判断参数的类型"""
    if isinstance(n, (int, float)) is isinstance(f, (int, float)):
        return True
    else:
        raise TypeError('非 int or float -> type 数据')

def division(f, n):
    """将-python-地板除法封装成一个函数.作用是可以多次使用"""
    return f / n

def char_type():
    """返回一个字符串"""
    return ".0"

def change_float(f, n):
    """将其结果转换成 float 类型返回"""
    return float(str(int(division(f, n))) + char_type())# 将这两个数的结果转换成整数后转换成字符串.最后将结果后面添加 一个 点 和 0 再转换成 浮点数

def Floor(f, n):
    """"""
    if deicde_type(f,n):
        if type(n) is int and type(f) is int:
            return int(division(f, n))# 直接转换成整形返回
        elif type(n) is int and type(f) is float:
            return change_float(f, n)
        elif type(n) is float and type(f) is int:# 不同的参数做的判断
            return change_float(f, n)
        else:
            return change_float(f, n)

if __name__ == "__main__":
    num = 3.0
    float_num = 333
    sum = Floor(float_num, num)
    print(type(sum))
    print(sum)# 输出结果: 111.0
    print("*"*20)
    print(Floor(19, 2))# 输出结果: 9
    print(Floor(16.0, 8))# 输出结果: 2.0
    print(Floor(888, 2.5))# 输出结果:355.0
