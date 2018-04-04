#!/usr/bin/env python
# filename: GenData.py
#

import time
import datetime
from random import randrange, choice
from string import ascii_lowercase as lc


def gen_data(doms, data_file):
    """
    generate data into file
    """
    with open(data_file, "w+") as f:
        # 100 about 12K, 40000000 about 4G
        for i in range(1, 100001):
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
            print(i, dtint, dtime, dtstr, dmail, file=f)


if __name__ == '__main__':
    tlds = ('com', 'edu', 'net', 'org', 'gov')
    data_f = "/tmp/datafile"

    startTime = time.time()
    gen_data(tlds, data_f)
    endTime = time.time()
    runTime = endTime - startTime
    print('runTime: {}'.format(runTime))
