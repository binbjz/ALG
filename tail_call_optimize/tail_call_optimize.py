#!/usr/bin/env python
# -*- coding: utf-8 -*-
# filename: tail_call_optimize.py
#
import sys


class TailRecurseException(Exception):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tail_call_optimized(g):
    """
    This function decorates a function with tail call
    optimization.
    """

    def func(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back \
                and f.f_back.f_back.f_code == f.f_code:
            raise TailRecurseException(args, kwargs)
        else:
            while 1:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException, e:
                    args = e.args
                    kwargs = e.kwargs

    func.__doc__ = g.__doc__

    return func


@tail_call_optimized
def tail_recursion(n, total=0):
    if n == 0:
        return total
    else:
        return tail_recursion(n - 1, total + n)


if __name__ == '__main__':
    print tail_recursion(1000000)
