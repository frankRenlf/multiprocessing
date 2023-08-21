# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : multiprocessing 
    @Product : PyCharm
    @createTime : 2023/8/21 21:27 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : small test
"""
from multiprocessing import Queue, Process


# if __name__ == "__main__":

def f(q):
    q.put([42, None, 'hello' * 10])
# def f(q):
#     q.put('X' * 1000000)


if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())  # prints "[42, None, 'hello']"
    p.join()

# if __name__ == '__main__':
#     queue = Queue()
#     p = Process(target=f, args=(queue,))
#     p.start()
#     p.join()  # this deadlocks
#     obj = queue.get()
