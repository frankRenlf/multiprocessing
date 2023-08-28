# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : multiprocessing 
    @Product : PyCharm
    @createTime : 2023/8/22 10:47 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""

# if __name__ == "__main__":
import multiprocessing
from time import sleep


def square(x):
    sleep(2)
    res = 0
    for i in range(x):
        res += i + i ** 2 + i ** 3
    return res


def main():
    data = reversed(range(10000, 10005))
    data3 = range(10000, 10005)
    data2 = reversed(range(10000, 10005))
    # 使用 map 方法
    with multiprocessing.Pool() as pool:
        print("map start")

        print("async start")
        results_async = [pool.apply_async(square, (x,)) for x in data2]
        print("async prcessing")

        result_map = pool.map(square, data)
        print("map processing")
        print("map success")

        result_apply_async = [result.get(timeout=3) for result in results_async]
        print("get success")

    print("Map result:", result_map)
    print("Apply Async result:", result_apply_async)
    # # 使用 apply_async 方法
    # with multiprocessing.Pool() as pool:
    #     print("async start")
    #     results_async = [pool.apply_async(square, (x,)) for x in data2]
    #     print("async prcessing")
    #     result_apply_async = [result.get(timeout=3) for result in results_async]
    #     print("get success")
    # print("Apply Async result:", result_apply_async)


if __name__ == "__main__":
    main()
