#!/usr/bin/env python
#filename: FindCommonK.py
#

"""
Searching two files for common lines and collecting their contents into set

a.txt
1,2,3,4
2,4,7,5
3,8,6,7
4,9,5,6
3,8,7,2

b.txt
1,2,4,6
2,3,6,5
3,8,9,2
4,9,6,9
3,5,2,3
6,2,7,3

results:
1,2(3,4,4,6)
3,8(6,7,7,2,9,2)
4,9(5,6,6,9)
"""

import datetime

Result = {}

def find_common_key(targetFile):
    with open(targetFile, 'r+') as file_handler:
        for line in file_handler:
            __line = map(int, line.strip().split(','))
            key = (__line[0], __line[1]); value = [__line[2], __line[3]]
            print 'key', key, ' -- ', 'value', value
            if key in Result:
                Result[key] = Result[key] + value
            else:
                Result[key] = value
    return Result


if __name__ == '__main__':
    files = ['a.txt', 'b.txt']
    print "Started At: ", datetime.datetime.now()
    print
    print 'Initial:'
    for f in files:
        find_common_key(f)

    print
    print "Write to Dic Finished At: ", datetime.datetime.now()

    print
    print 'Result:'
    for k, v in Result.items():
        if len(v) > 2:
            #print k, v
            print ','.join(map(str, k)), tuple(v)

    print
    print "Finished At: ", datetime.datetime.now()
