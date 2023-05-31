#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/24 21:07
# @Author  : cap669
# @File    : MyApp.py
# @Software: PyCharm
from kazuya.era.XRsa import XRsa,RsaInject
from fastapi import FastAPI

from server.conf.ServerConf import serverconf
from server.fragment.HapFragment import HapFragment
from server.bis.EioBis import EioBis
@RsaInject(serverconf.host,serverconf.port)
class MyApp(XRsa):
    def __init__(self):
        XRsa.__init__(self)

    def base(self):
        pass

    def utils(self):
        pass

    def rpc(self):
        pass

    def bis(self):
        self.eio = EioBis()

    def fragment(self,app:FastAPI):
        HapFragment(app,self.eio)

if __name__ == '__main__':
    MyApp()