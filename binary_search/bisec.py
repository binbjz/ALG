#!/usr/bin/env python
# filename: bisec.py
#

import bisect


def bisec(lst, item):
    low, high = 0, len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = lst[mid]

        if item == mid_val:
            return mid

        if item > mid_val:
            low = mid + 1
        else:
            high = mid - 1
    raise ValueError

    
def bisec_(lst, x):
    i = bisect.bisect_left(lst, x)
    if i != len(lst) and lst[i] == x:
        return i
    raise ValueError

def bisec_left(lst, item):
    low, high = 0, len(lst)

    while low < high:
        mid = (low + high) // 2
        mid_val = lst[mid]

        if item > mid_val:
            low = mid + 1
        else:
            high = mid
    return low


def bisec_right(lst, item):
    low, high = 0, len(lst)

    while low < high:
        mid = (low + high) // 2
        mid_val = lst[mid]

        if item < mid_val:
            high = mid
        else:
            low = mid + 1
    return low


def bisec_2d(lsts, x):
    meta = [lst[-1] for lst in lsts]
    # i1 = bisect.bisect_left(meta, x)
    i1 = bisec_left(meta, x)

    if i1 != len(meta):
        lst = lsts[i1]
        # i2 = bisect.bisect_left(lst, x)
        i2 = bisec_left(lst, x)
        if i2 != len(lst) and lst[i2] == x:
            return i1, i2
    raise ValueError


if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 12]
    v = 9
    print("{} => {}".format(v, bisec(lst, v)))
    print("{} => {}".format(v, bisec_left(lst, v)))
    print("{} => {}".format(v, bisec_right(lst, v)))

    lsts = [[1, 4, 5], [7, 8, 9, 10], [11, 12, 14, 15]]
    print("{} => {}".format(v, bisec_2d(lsts, v)))
