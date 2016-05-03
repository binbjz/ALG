#!/usr/bin/env python
#filename: PascalTriangle_enh.py
#

import datetime

def pascal(n):
    """
    Yield up to row ``n`` of Pascal's triangle, one row at a time.

    The first row is row 0.

    >>> list (pascal (0))
    [ [1] ]
    >>> list (pascal (1))
    [ [1], [1, 1]]
    >>> list (pascal (4))
    [ [1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1] ]
    >>> list (pascal (-1))
    Traceback (most recent call last):
    ValueError: n must be an integer >= 0
    """
    if not isinstance(n, int):
        raise TypeError('n must be an integer')
    if n < 0:
        raise ValueError('n must be an integer >= 0')

    def newrow(row):

        "Calculate a row of Pascal's triangle given the previous one."
        prev = 0
        for x in row:
            yield prev + x
            prev = x
        yield 1

    prevrow = [1]
    yield prevrow
    for x in xrange(n):
        prevrow = list(newrow(prevrow))
        yield prevrow


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    for i in pascal(5):
        print i
    end_time = datetime.datetime.now()
    print '\nrunning_time: %d microsecond' % (int(str(end_time).split('.')[-1]) - int(str(start_time).split('.')[-1]))
