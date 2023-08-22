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
    pool.close()


def loop(v, l, num):
    l.acquire()
    for i in range(10):
        time.sleep(0.1)
        v.value += num
        print(v.value)
    l.release()


def golbal_val():
    l = mp.Lock()
    v = mp.Value('i', 0)
    p1 = mp.Process(target=loop, args=(v, l, 1))
    p2 = mp.Process(target=loop, args=(v, l, 3))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


import multiprocessing


# 定义一个函数，作为多进程任务
def worker_function(task_id):
    # print(f"Task {task_id} is being processed by process {multiprocessing.current_process().name}")
    current_process = mp.current_process()
    print(f"Process Name: {current_process.name}")
    print(f"Process ID: {current_process.pid}")
    res = 0
    for i in range(100000):
        res += i + i ** 2 + i ** 3


def mul_test():  # 创建进程池，指定进程数量
    num_processes = 4
    pool = multiprocessing.Pool(processes=num_processes)

    # 定义任务列表
    tasks = [i for i in range(100, 120 + 1)]

    # 使用进程池执行任务
    pool.map(worker_function, (tasks))

    # 关闭进程池，不再接受新任务
    pool.close()

    # 等待所有任务完成
    pool.join()

    print("All tasks have been completed.")


def print_process_info():
    current_process = mp.current_process()
    print(f"Process Name: {current_process.name}")
    print(f"Process ID: {current_process.pid}")


#
if __name__ == "__main__":
    # golbal_val()
    # muti_pool()
    # pool = mp.Pool()
    # result = pool.map_async(func=fn_1, iterable=range(100))
    # result2 = pool.map_async(func=fn_1, iterable=range(2))
    # result.get()
    # result2.get()
    # mp.set_start_method('spawn')
    # mul_test()
    golbal_val()
