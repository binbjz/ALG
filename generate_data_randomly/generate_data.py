#!/usr/bin/env python
#filename: generate_data.py
#

import time,datetime
from random import randrange, choice
from string import ascii_lowercase as lc

tlds = ('com', 'edu', 'net', 'org', 'gov')

# speficy the location of the generated file
f=open("/tmp/datafile","w+")
startTime = time.time()

#100 about 12K, 40000000 about 4G
for i in range(1,100001):
    dtint = randrange(2**52)
    now = datetime.datetime.now()
    dtime = now.strftime("%Y%m%d-%H:%M:%S.%f")

    llen = randrange(4,8)
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)
    dom = ''.join(choice(lc) for j in xrange(dlen))
    suff = choice(tlds)
    dmail = login + '@' + dom + '.' + suff

    dtstr=''.join(choice(lc) for j in range(randrange(20,22)))
    print >> f,i,dtint,dtime,dtstr,dmail
f.close()

endTime = time.time()
runTime = endTime - startTime
print 'runTime: ', runTime
