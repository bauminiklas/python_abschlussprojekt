from PyQt4 import QtGui

class ReferenceBogenUI(QtGui.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)


    def mousePressEvent(self, event):
        p = event.pos()
        lst = [p.x(), p.y()]
        print(lst)