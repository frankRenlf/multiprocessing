# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : multiprocessing 
    @Product : PyCharm
    @createTime : 2023/8/22 12:01 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""

# if __name__ == "__main__":
from multiprocessing import Process, Manager


def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()


def f2(v):
    v.value = 2


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))
        v = manager.Value('i', 1)
        p = Process(target=f, args=(d, l))
        p2 = Process(target=f2, args=(v,))
        p.start()
        p2.start()
        p.join()
        p2.join()
        print(d)
        print(l)
        print(v.value)
