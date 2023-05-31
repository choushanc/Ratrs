#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/27 19:54
# @Author  : cap669
# @File    : EioBis.py
# @Software: PyCharm
import time
from kazuya.plux.XClient import XClient, XState, ClientBone
from string import ascii_uppercase
from typing import Dict
a0 = list(ascii_uppercase)
b0 = 0
c0 = 0
class EioBis(XClient):
    def __init__(self):
        XClient.__init__(self)

    def abraham_login(self, us: str, pw: str, state: XState):
        global b0
        c0 = a0[b0]
        b0 += 1
        state.succ(1)
        return c0, c0

    def abraham_client(self, cb: ClientBone):
        global c0
        cb.data.update({'ff':c0})
        c0 += 1
        time.sleep(1)

    def tx0(self,aka:str,por:str):
        @self.clientmanage.cheack_client
        def saia0(cb:ClientBone,state:XState):
            return cb.state
        return saia0(aka=aka,por=por)

    async def abraham_call(self,act:str,data:Dict,cb:ClientBone):
        print(cb.data,'sfafw')