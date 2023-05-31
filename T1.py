#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/31 10:13
# @Author  : cap669
# @File    : T1.py
# @Software: PyCharm


# https://192.168.31.208:8085
def ues(cpath="C:\Program Files\Google\Chrome\Application",port=9222,spath="C:\mfw"):
    return 'cd {} && chrome.exe --disable-web-security --remote-debugging-port={} --user-data-dir="{}"'.format(cpath,port,spath)

print(ues())



