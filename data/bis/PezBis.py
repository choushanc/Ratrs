import time

from kazuya.kant.TywKant import TywKant,Job2Cur,XState,Job2Model
from data.base.Cur import database
class PezCur(Job2Cur):
    class Meta:
        database = database
        table_name = 'jian2'

class PezBis(TywKant):
    def __init__(self):
        TywKant.__init__(self,PezCur)

    def fist_range(self):
        from string import ascii_uppercase
        self.xjob2.add_jobs(list(ascii_uppercase))

    def muta_set(self,aka,d0:Job2Model,state:XState,*args,**kwargs):
        # print(aka,d0.__dict__,'set')
        time.sleep(1)
        return 10,0

    def muta_func(self,aka:str,d0:Job2Model,state:XState,*args,**kwargs):
        # print(aka,d0.__dict__,'func')
        state.succ(4)
        time.sleep(1)

    def stop_job(self,job:str,state:XState):
        self.xjob2.stop_job(job)

    def end_job(self, state: XState):
        pass