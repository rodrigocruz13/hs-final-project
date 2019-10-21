#!/usr/bin/env python3
from multiprocessing import Pool
import os

def f(x):
    print("Input {} in process {}".format(x, os.getpid()))
    #print(x)
    return -x

if __name__ == '__main__':
    with Pool(905) as p:
        results = p.map(f, range(905))
    print(type(results))