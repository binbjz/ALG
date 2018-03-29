#!/usr/bin/env python
# filename: FindCommonK.py
#

"""
ds1.txt
1,2,3,4,7
2,4,7,5,9,12
3,8,6,7
4,9,5,6
3,8,7,2

ds2.txt
1,2,4,6
2,3,6,5
3,8,9,2
4,9,6,9,12
3,5,2,3
6,2,7,3
"""

import datetime


class FindCommKey(object):
    def __init__(self):
        self.combine = {}
        self.counter = {}
        self.result = {}

    def find_common_key(self, target_file):
        with open(target_file, 'r+') as file_handler:
            for line in file_handler:
                print(line, end='')
                __line = list(map(int, line.strip().split(',')))
                key, value = tuple(__line[:2]), __line[2:]
                if key in self.combine:
                    self.combine[key] = self.combine[key] + value
                else:
                    self.combine[key] = value

                if key in self.counter:
                    self.counter[key] = self.counter[key] + 1
                else:
                    self.counter[key] = 1

        for k1, v1 in self.counter.items():
            if v1 >= 2:
                self.result[k1] = self.combine[k1]
        print()
        return self.result


if __name__ == '__main__':
    files = ['ds1.txt', 'ds2.txt']
    print("Started at: {}{}".format(datetime.datetime.now(), '\n'))
    print('Initial data:')
    fck = FindCommKey()
    for f in files:
        fck.find_common_key(f)

    print("Write to dic finished at: {}{}".format(datetime.datetime.now(), '\n'))

    print('Result set:')
    for k, v in fck.result.items():
        print(','.join(map(str, k)), tuple(v))
    print("{}Finished at: {}".format('\n', datetime.datetime.now()))
