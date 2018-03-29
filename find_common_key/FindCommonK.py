#!/usr/bin/env python
# filename: FindCommonK.py
#

import datetime


class FindCommKey(object):
    def __init__(self):
        self.combine = {}
        self.counter = {}
        self.result = {}

    def find_common_key(self, target_file):
        with open(target_file, 'r+') as file_handler:
            for line in file_handler:
                __line = list(map(int, line.strip().split(',')))
                print(__line)
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
    files = ['a.txt', 'b.txt']
    print("Started at: {}".format(datetime.datetime.now()))
    print()
    print('Initial data:')
    fck = FindCommKey()
    for f in files:
        fck.find_common_key(f)

    print()
    print("Write to dic finished at: {}".format(datetime.datetime.now()))

    print()
    print('Result set:')
    for k, v in fck.result.items():
        print(','.join(map(str, k)), tuple(v))
    print()
    print("Finished at: {}".format(datetime.datetime.now()))
