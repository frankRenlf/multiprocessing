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
import time


def fn_1(n):
    res = 0
    for i in range(n):
        res += i + i ** 2 + i ** 3
    return res


def normal(n):
    p_arr = [] * n
    v_arr = [0] * n
    for i in range(n):
        v_arr[i] = fn_1(100000)
    for i in range(n):
        a = 1
    for i in range(n):
        b = 1
    for i in range(n):
        b = 1


def fn_m(q, n):
    res = 0
    for i in range(n):
        res += i + i ** 2 + i ** 3
    q.put(res)


def multiPro(n):
    q = mp.Queue()
    p_arr = []
    v_arr = [0] * n
    for i in range(n):
        p_arr.append(mp.Process(target=fn_m, args=(q, 100000)))
    for i in range(n):
        p_arr[i].start()
    for i in range(n):
        p_arr[i].join()
    for i in range(n):
        v_arr[i] = q.get()


def compare_(n):
    t1_s = time.time()
    normal(n)
    t1_e = time.time()
    print('time cost', t1_e - t1_s, 's')
    t2_s = time.time()
    multiPro(n)
    t2_e = time.time()
    print('time cost', t2_e - t2_s, 's')


def job(x):
    return x * x


def muti_pool():
    pool = mp.Pool()
    res = pool.map(job, range(10))
    print(res)
    res2 = pool.apply_async(job, (1,))
    print(res2.get())


def loop(v, num):
    for i in range(10):
        v.value += num


def golbal_val():
    v = mp.Value('i', 1)
    p1 = mp.Process(target=loop, args=(v, 1))
    p2 = mp.Process(target=loop, args=(v, 3))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(v.value)


if __name__ == "__main__":
    golbal_val()
