from data.bis.QieBis import QieBis
from data.bis.MiaBis import MiaBis
from data.bis.PezBis import PezBis
from kazuya.XState import XState
from kazuya.era.XEva import XEva
from PySide6.QtWidgets import QApplication
class MyApp(XEva):
    def __init__(self):
        XEva.__init__(self)

    def base(self):
        pass

    def utils(self):
        pass

    def rpc(self):
        pass

    def bis(self):
        self.mia = MiaBis()
        # self.qie = QieBis()
        # self.pez = PezBis()

    def register_func(self,state:XState,*args,**kwargs):
        self.mia.run(3,state)
        # self.qie.run(3,state)
        # self.pez.run(3,state)

if __name__ == '__main__':

    app = QApplication([])
    widget = MyApp()
    widget.show()
    app.exec()
