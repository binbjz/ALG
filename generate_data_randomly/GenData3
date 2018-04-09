#!/usr/bin/env python
# filename: GenData3.py
#

import os
import sys
import time
import datetime
from random import randrange, choice
from string import ascii_lowercase as lc


class GenData3(object):
    def __init__(self, stdout='/dev/null', stderr='/dev/null'):
        self.stdout = stdout
        self.stderr = stderr

    # Generate data into file
    def gen_data(self, doms, number_of_rows=1000001):
        # Flush I/O buffers
        sys.stdout.flush()

        with open(self.stdout, 'ab', 0) as f:
            os.dup2(f.fileno(), sys.stdout.fileno())

        # 100 about 12K, 40000000 about 4G
        for i in range(1, number_of_rows):
            dtint = randrange(2 ** 52)
            now = datetime.datetime.now()
            dtime = now.strftime("%Y%m%d-%H:%M:%S.%f")

            llen = randrange(4, 8)
            login = ''.join(choice(lc) for j in range(llen))
            dlen = randrange(llen, 13)
            dom = ''.join(choice(lc) for j in range(dlen))
            suff = choice(doms)
            dmail = login + '@' + dom + '.' + suff

            dtstr = ''.join(choice(lc) for j in range(randrange(20, 22)))
            sys.stdout.write('{} {} {} {} {}\n'.format(i, dtint, dtime, dtstr, dmail))


if __name__ == '__main__':
    data_f = '/tmp/datafile'
    tlds = ('com', 'edu', 'net', 'org', 'gov')
    gd = GenData3(stdout=data_f)

    startTime = time.time()
    gd.gen_data(tlds)
    endTime = time.time()
    runTime = endTime - startTime
    sys.stderr.write('runTime: {}\n'.format(runTime))
