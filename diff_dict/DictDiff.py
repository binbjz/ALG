#!/usr/bin/env python
#filename: DictDiff.py
#

KEYNOTFOUND = '<KEYNOTFOUND>'

class dict_cls(object):
    @staticmethod
    def dict_diff(first, second):
        """ Return a dict of keys that differ with another config object.  If a value is
            not found in one of the configs, it will be represented by KEYNOTFOUND.
            @param first:   Fist dictionary to diff.
            @param second:  Second dicationary to diff.
            @return diff:   Dict of Key => (first.val, second.val)
        """
        diff = {}

        # Check all keys in first dict
        for key in first.keys():
            if (not second.has_key(key)):
                diff[key] = (first[key], KEYNOTFOUND)
            elif (first[key] != second[key]):
                diff[key] = (first[key], second[key])

        # Check all keys in second dict to find missing
        for key in second.keys():
            if (not first.has_key(key)):
                diff[key] = (KEYNOTFOUND, second[key])
        return diff

if __name__ == '__main__':
    dict1 = {1:'student', 2:'teacher', 3:'friend'}
    dict2 = {1:'student', 2:'teacher', 3:'friend'}

    dict3 = {11:'student', 12:'teacher', 13:'friend'}
    dict4 = {11:'students', 12:'teachers', 13:'friends'}

    dict5 = {21:'student', 22:'teacher', 23:'friend'}
    dict6 = {21:'students', 22:'teachers', 23:'friends'}

    print dict_cls.dict_diff(dict1, dict2)
    print dict_cls.dict_diff(dict4, dict3)
    print dict_cls.dict_diff(dict5, dict6)
    print dict_cls.dict_diff(dict5, dict3)
