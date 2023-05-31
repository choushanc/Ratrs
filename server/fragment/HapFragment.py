#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/25 22:36
# @Author  : cap669
# @File    : HapFragment.py
# @Software: PyCharm
from kazuya.plux.XFragment import XFragment
from fastapi import APIRouter, FastAPI, WebSocket, WebSocketDisconnect
from server.bis.EioBis import EioBis
from kazuya.plux.XClient import LoginModel, AuthModel


class HapFragment(XFragment):
    def __init__(self, app: FastAPI, eio: EioBis):
        XFragment.__init__(self, '/hap', app)
        self.eio = eio

    def register_router(self, router: APIRouter):
        # stun - fli - gram - mig - ait - zaff - kaim - rork - tosh
        def login():
            @router.post('/login')
            async def yasm(d0: LoginModel):
                return self.eio.login0(d0)

            @router.get('/login')
            async def klir(us: str = 'A', pw: str = 'A'):
                return self.eio.login1(us, pw)

        login()

        @router.post('/tx0')
        async def tx0(d0: AuthModel):
            return self.eio.tx0(d0.aka, d0.por)

        def keep():
            @router.post('/keep')
            async def douk(d0: AuthModel):
                pass

            @router.post('/keep')
            async def nout(d0: AuthModel):
                pass

        keep()

        @router.websocket('/bans/{aka}')
        async def bans(ws: WebSocket, aka: str):
            await self.eio.websocket(ws, aka)

        def stop():
            @router.post('/stop')
            async def phu():
                pass

            @router.get('/stop')
            async def dend():
                pass

        stop()

        @router.get('/ass')
        async def ass():
            return {
                "Code": 0,
                "Msg": "",
                "Data": [
                    dict(aa='a', bb=s) for s in range(5)
                ]
            }
