def loop(count):
    cdef int a = 0
    for i in xrange(count):
        for e in xrange(i):
            a += 1
    return a
