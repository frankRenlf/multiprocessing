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

from multiprocessing import Process, Pipe


def f(conn, num):
    conn.send([42, num, 'hello'])
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(parent_conn, 1))
    p2 = Process(target=f, args=(child_conn, 2))
    p.start()
    p2.start()
    print(parent_conn.recv())  # prints "[42, None, 'hello']"
    print(child_conn.recv())  # prints "[42, None, 'hello']"
    p.join()
    p2.join()
