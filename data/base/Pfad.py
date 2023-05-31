#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/31 9:13
# @Author  : cap669
# @File    : Pfad.py
# @Software: PyCharm
from kazuya.plux.XPath import XPath
from pathlib import Path
class Pfad(XPath):
    def __init__(self):
        XPath.__init__(self)

    def abraham_path(self,simp_path,hard_path,real_path):
        self.tdx_path:Path = hard_path(r'C:\Dat\Ratrs')
        self.szzs = real_path(self.tdx_path.joinpath('SH#999999.txt'))


pfad = Pfad()

