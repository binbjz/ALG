#!/usr/bin/env python
# filename: TailRecurse.py
#
# This program shows off a python decorator(
# which implements tail call optimization. It
# does this by throwing an exception if it is
# it's own grandparent, and catching such
# exceptions to recall the stack.
#
import cProfile
import functools
import sys
import timeit
import traceback


class TailRecurseException(Exception):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tail_call_optimized(g):
    """
    This function decorates a function with tail call
    optimization. It does this by throwing an exception
    if it is it's own grandparent, and catching such
    exceptions to fake the tail call optimization.

    This function fails if the decorated
    function recurses in a non-tail context.
    """

    @functools.wraps(g)
    def func(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back \
                and f.f_back.f_back.f_code == f.f_code:
            raise TailRecurseException(args, kwargs)
        else:
            while 1:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs

    # func.__doc__ = g.__doc__
    return func


@tail_call_optimized
def tail_recursion(n, total=1):
    if n == 1:
        return total
    else:
        return tail_recursion(n - 1, total + n)


def fact(n, total=1):
    traceback.print_stack(file=sys.stdout)  # prints the current stack

    while True:  # change recursion to a while loop
        if n == 1:
            return total
        n, total = n - 1, total * n


def cum_sum(n, total=1):
    while True:  # change recursion to a while loop
        if n == 1:
            return total
        n, total = n - 1, total + n  # update parameters instead of tail recursion


if __name__ == '__main__':
    print("{}".format(tail_recursion(12600000)))
    print("{}".format(cum_sum(126000000)))

    result = fact(126000)
    print("{} length is {}".format(result, len(str(result))))

    # 1260000 - py365 - 282 function calls in 716.046 seconds
    # 1260000 - py2714 - 89 function calls in 717.982 seconds
    cProfile.run('result = fact(126000)')
    print(timeit.timeit('result = fact(126000)', "from __main__ import fact", number=3))
