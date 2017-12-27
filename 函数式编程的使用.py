# coding:utf-8

def box():
    """"""
    return [1, 2, 30, -1, -232, 'aadsf','werw', 'tafsf', '2342', 343, 'gg', 'fff']

def main(box):
    """"""
    for item in box:
        if handle(item):
            printf()()(item)

def printf():
    """"""
    def function():
        """"""
        return lambda item: print('处理过剩余的参数都有_', item)
    return function

def handle(item):
    """"""
    if isinstance(item, int):
        if item > 3:
            return True
    elif isinstance(item, str):
        if len(item) <= 3:
            return True

    return False

if __name__ == "__main__":
    main(box())