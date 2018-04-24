#!/usr/bin/env python
# filename: GenData2.py
#

import datetime
import cProfile
from contextlib import redirect_stdout
from random import randrange, choice
from string import ascii_lowercase as lc


class GenData2(object):
    def __init__(self, doms, data_file, number_of_rows=1000001):
        self.doms = doms
        self.data_file = data_file
        self.number_of_rows = number_of_rows

    # Generate data into file
    def gen_data(self):
        with open(self.data_file, "w") as f:
            with redirect_stdout(f):
                # 100 about 12K, 40000000 about 4G
                for i in range(1, self.number_of_rows):
                    dtint = randrange(2 ** 52)
                    now = datetime.datetime.now()
                    dtime = now.strftime("%Y%m%d-%H:%M:%S.%f")

                    llen = randrange(4, 8)
                    login = ''.join(choice(lc) for j in range(llen))
                    dlen = randrange(llen, 13)
                    dom = ''.join(choice(lc) for j in range(dlen))
                    suff = choice(self.doms)
                    dmail = login + '@' + dom + '.' + suff

                    dtstr = ''.join(choice(lc) for j in range(randrange(20, 22)))
                    print('{} {} {} {} {}'.format(i, dtint, dtime, dtstr, dmail))


if __name__ == '__main__':
    data_f = '/tmp/datafile'
    tlds = ('com', 'edu', 'net', 'org', 'gov')
    gd = GenData2(tlds, data_f)
    cProfile.run('gd.gen_data()')
