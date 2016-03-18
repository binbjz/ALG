#!/usr/bin/env python
#coding=utf-8
#filename: total-monitor.py
#

import os
import re
import datetime
import pyinotify
import logging

class MyEventHandler(pyinotify.ProcessEvent):
    # Specify the log directory
    logging.basicConfig(level=logging.INFO,
                       filename='/mnt/tmpfs/monitor.log'
                       )
    logging.info("Starting monitor...")

    def process_IN_ACCESS(self, event):
        self.rebuild("ACCESS event", event)

    def process_IN_ATTRIB(self, event):
        self.rebuild("ATTRIB event", event)

    def process_IN_CLOSE_NOWRITE(self, event):
        self.rebuild("CLOSE_NOWRITE event", event)

    def process_IN_CLOSE_WRITE(self, event):
        self.rebuild("CLOSE_WRITE event", event)

    def process_IN_CREATE(self, event):
        self.rebuild("CREATE event", event)

    def process_IN_DELETE(self, event):
        self.rebuild("DELETE event", event)

    def process_IN_MODIFY(self, event):
        self.rebuild("MODIFY event", event)

    def process_IN_OPEN(self, event):
        self.rebuild("OPEN event", event)

    def rebuild(self, event_name, event):
        # specify excluding files suffix
        patt=r"\.txt$|\.swp$|\.swx"

        exclude_filter=re.compile(patt)
        if re.search(patt, event.pathname) is None:
            print "%s:" % event_name, event.pathname
            logging.info("%s : %s  %s" % (event_name,os.path.join(event.path,event.name),datetime.datetime.now()))


def main():
    wm = pyinotify.WatchManager()

    # Specify the directory for monitoring, for example: /tmp
    wm.add_watch('/tmp', pyinotify.ALL_EVENTS, rec=True)
    eh = MyEventHandler()

    notifier = pyinotify.Notifier(wm, eh)
    notifier.loop()

if __name__ == '__main__':
    main()
