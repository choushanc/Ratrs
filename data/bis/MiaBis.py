import time

from kazuya.kant.PazKant import PazKant, Job0Cur, XState, Job0Model
from ..base.Cur import database


class MiaCur(Job0Cur):
    class Meta:
        database = database
        table_name = 'jian0'


class MiaBis(PazKant):
    def __init__(self):
        PazKant.__init__(self, MiaCur)

    def muta_diff(self, d0: Job0Model, state: XState):
        diff = 2
        if d0.diff == diff:
            state.succ(2)
        else:
            state.succ(8)
        return diff

    def muta_func(self, d0: Job0Model, state: XState):
        state.succ(5)
        time.sleep(1)

    def fist_range(self):
        from string import ascii_uppercase
        self.xjob0.add_jobs(list(ascii_uppercase))

    def end_job(self, state: XState):
        pass

    def stop_job(self, job: str, state: XState):
        self.xjob0.stop_job(job)
