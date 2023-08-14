# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : multiprocessing 
    @Product : PyCharm
    @createTime : 2023/8/14 20:21 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : process
"""

import multiprocessing as mp


def fn_1(q, n):
    res = 0
    for i in range(n):
        res += i + i ** 2 + i ** 3
    q.put(res)


if __name__ == "__main__":
    q = mp.Queue()

    p1 = mp.Process(target=fn_1, args=(q, 1000))
    p1.start()
    p1.join()
