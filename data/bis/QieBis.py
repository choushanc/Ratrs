from kazuya.kant.VetcKant import VetcKant, Job1Cur, XState, JobModel
from data.base.Cur import database
import time


class QieCur(Job1Cur):
    class Meta:
        database = database
        table_name = 'jian1'


class QieBis(VetcKant):
    def __init__(self):
        VetcKant.__init__(self, QieCur)

    def fist_range(self):
        from string import ascii_uppercase
        self.xjob1.add_jobs(list(ascii_uppercase))

    def muta_func(self, d0: JobModel, state: XState, *args, **kwargs):
        state.succ(7)
        time.sleep(1)

    def end_job(self, state: XState):
        pass
