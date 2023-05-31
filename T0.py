#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/30 12:11
# @Author  : cap669
# @File    : T0.py
# @Software: PyCharm
import time

from websocket import WebSocketApp
from threading import Thread
from json import dumps
class T0:
    def __init__(self):
        self.ws = WebSocketApp('ws://192.168.31.208:8877/hap/bans/A',on_open=self.on_open)
        self.ws.run_forever()


    def on_open(self):
        def saia0():
            js = 0
            while js < 20:
                self.ws.send(dumps(dict(act='keec',data={})))
                time.sleep(1)
                js += 1


        Thread(target=saia0).start()
T0()