# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : multiprocessing 
    @Product : PyCharm
    @createTime : 2023/8/22 11:14 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""

# if __name__ == "__main__":

from multiprocessing import Process, Value, Array


def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] -= a[i]


if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
