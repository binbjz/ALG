#!/usr/bin/env python
#filename: singleton.py
#

class Singleton(object):
    __single = None
    def __new__(clz):
        if not Singleton.__single:
            #Singleton.__single = object.__new__(clz)
            Singleton.__single = super(Singleton, clz).__new__(clz)
        return Singleton.__single
        
    def doSomething(self):
        print("do something...XD")

singleton = Singleton()
singleton.doSomething()
