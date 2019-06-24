#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time

class myThread(threading.Thread):
    def _init_(self,threadID,name,counter):
        threading.Thread._init_(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        