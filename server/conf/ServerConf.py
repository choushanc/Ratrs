#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/30 15:24
# @Author  : cap669
# @File    : ServerConf.py
# @Software: PyCharm
from pydantic import BaseSettings
from functools import lru_cache
from Config import env
class ServerConfig(BaseSettings):
    host: str = '127.0.0.1'
    port: int =7788
class DevServerConfig(ServerConfig):
    host = '192.168.31.123'
    port = 7788
class ProServerConfig(ServerConfig):
    host = '192.168.31.208'
    port = 8877

@lru_cache()
def register_config() -> ServerConfig:
    return dict(
        dev=DevServerConfig,
        pro=ProServerConfig,
    )[env]()


serverconf = register_config()

