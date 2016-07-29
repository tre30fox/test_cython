# coding=utf8

import sys
import time
import pyximport
pyximport.install()
pyximport.install()
pyximport.install()
import auto_build


def loop(count):
    
    a = 0
    for i in xrange(count):
        for e in xrange(i):
            a += 1
    return a

if __name__ == '__main__':
    start = time.time()
    print loop(int(sys.argv[-1]))
    mid = time.time()
    print auto_build.loop(int(sys.argv[-1]))
    end = time.time()
    
    print start, mid, end
    print mid - start, end - mid
